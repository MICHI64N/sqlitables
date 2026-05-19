import sqlite3

class ColumnConstraint:
    def __init__(self, name: str, value: str | None):
        self.name = name
        self.value = value

class Column:
    def __init__(self, name: str, datatype: str, constraints: list[ColumnConstraint] | None):
        self.name = name
        self.datatype = datatype
        self.constraints = constraints
    def statement(self):
        statement = f'"{self.name}" {self.datatype}'
        if self.constraints:
            for constraint in self.constraints:
                statement += f' {constraint.name}'
                if constraint.value:
                    statement += f' {constraint.value}'
        return statement

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
            sql += column.statement()
            if index != len(self.columns) - 1: sql += ', '
        sql += ');'
        cursor.execute(sql)
    def insert_into(self, values: list[tuple[str, int, None]], cursor: sqlite3.Cursor):
        sql = f'INSERT INTO "{self.name}" VALUES '
        for index, value in enumerate(values):
            sql += '('
            if type(value) == tuple:
                for index, field in enumerate(value):
                    sql += str(field)
                    if index != len(value) - 1: sql += ', '
            else:
                sql += str(value)
            sql += ')'
            if index != len(values) - 1: sql += ', '
        sql += ';'
        cursor.execute(sql)