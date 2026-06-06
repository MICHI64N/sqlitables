import sqlite3
import re

class Column:
    def __init__(self, name: str, datatype: str):
        self.name = name
        self.datatype = datatype
        self.constraints = []

    def constraint(self, constraint: str, value: str | int | float | None):
        valid_constraints = ["check", "collate", "default", "not null", "primary key", "unique"]
        if constraint.lower() in valid_constraints:
            self.constraints.append((constraint, value))

    def _definition_constraint_value(self, value):
        definition = ""
        if type(value) == str and not re.match(r'^\(.+\)$', value): # escapes strings and parses expressions
            definition += f'"{value}"'
        else:
            definition += f'{value}'
        return definition
    def _definition_constraint(self, constraint, value):
        definition = f'{constraint}' # constraint name
        if value:
            definition += f' {self._definition_constraint_value(value)}'
        return definition
    def definition(self): # This definition is used for table creation
        definition = f'"{self.name}" {self.datatype}'
        if len(self.constraints) >= 1:
            for constraint in self.constraints:
                definition += f' {self._definition_constraint(constraint[0], constraint[1])}'
        return definition

class Table:
    def __init__(self, name: str, columns: list[Column]):
        self.name = name
        self.columns = columns

    def exists(self, cursor: sqlite3.Cursor):
        sql = f'SELECT name FROM sqlite_master WHERE type="table" AND name="{self.name}";'
        find = cursor.execute(sql)
        exists = True if find.fetchone() else False
        return exists
    
    def create(self, cursor: sqlite3.Cursor):
        sql = f'CREATE TABLE "{self.name}"( '
        for index, column in enumerate(self.columns):
            sql += column.definition()
            if index != len(self.columns) - 1: sql += ', '
        sql += ');'
        cursor.execute(sql)

    def _insert_column(self, field: str):
        if type(field) == str:
            sql = f'"{field}"'
            if field.lower() == "null":
                sql = 'NULL'
        else:
            sql = str(field)
        return sql
    def _insert_one(self, value: tuple):
        sql = '('
        for index, field in enumerate(value): # enumerate tuple
            sql += self._insert_column(field)
            if index != len(value) - 1: sql += ', '
        sql += ')'
        return sql
    def insert(self, values: list[tuple], connection: sqlite3.Connection):
        sql = f'INSERT INTO "{self.name}" VALUES '
        for index, value in enumerate(values): # enumerate list
            sql += self._insert_one(value)
            if index != len(values) - 1: sql += ', '
        sql += ';'
        connection.cursor().execute(sql).close()
        connection.commit()

    def _select_str(self, select: str):
        if select == "*":
            sql = f'*'
            return sql
        else:
            raise ValueError('The select parameter can only include a list of Column objects or "*".')
    def _select_columns(self, select: list[Column]):
        sql = ''
        for index, col in enumerate(select):
            sql += f'"{col.name}"' 
            if index != len(select) - 1: sql += ', '
        return sql
    def select(self, select: list[Column] | str, where: str | None, cursor: sqlite3.Cursor):
        # SELECT [select]
        sql = 'SELECT '
        if type(select) == str:
            sql += self._select_str(select)
        else:
            sql += self._select_columns(select) # type: ignore ;; reads col a possible string when it is not.
        # FROM table
        sql += f' FROM "{self.name}"'
        # WHERE [where]
        if where:
            sql += f' WHERE {where}'
        sql += ";"
        # Selection
        selection = cursor.execute(sql)
        return selection.fetchall()