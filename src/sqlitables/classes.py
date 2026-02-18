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
            if index != len(self.columns) - 1: ", "
        sql += " );"
        cursor.execute(sql)