import sqlite3

class Column:
    def __init__(self, name: str, datatype: str):
        self.name = name
        self.datatype = datatype
    def statement(self):
        statement = f'"{self.name}" {self.datatype}'
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
    def insert(self, values: list[tuple], connection: sqlite3.Connection):
        sql = f'INSERT INTO "{self.name}" VALUES '
        for index, value in enumerate(values): # enumerate list
            sql += '('
            for tupleindex, field in enumerate(value): # enumerate tuple
                if type(field) == str:
                    sql += f'"{field}"'
                else:
                    sql += str(field)
                if tupleindex != len(value) - 1: sql += ', '
            sql += ')'
            if index != len(values) - 1: sql += ', '
        sql += ';'
        connection.cursor().execute(sql).close()
        connection.commit()
    def select(self, select: list[Column] | str, where: str | None, cursor: sqlite3.Cursor):
        sql = 'SELECT '
        if type(select) == str:
            if select == "*":
                sql += f'* FROM {self.name}'
            else:
                raise ValueError('The select parameter can only include a list of Column objects or "*".')
        else:
            for index, col in enumerate(select):
                sql += f'"{col.name}"' # type: ignore ;; reads col a possible string when it is not.
                if index != len(select) - 1: sql += ', '
            sql += f' FROM {self.name}'
        if where:
            sql += f' WHERE {where}'
        sql += ";"
        selection = cursor.execute(sql)
        return selection.fetchall()