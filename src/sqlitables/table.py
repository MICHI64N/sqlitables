"""Defines the classes that make up a table.

Attributes:
    DATATYPE (Literal["BLOB", "INTEGER", "NUMERIC", "REAL", "TEXT"]):
        Datatype affinities in SQLite.
"""

import sqlite3 # I will need this again later...
from typing import Literal, get_args

DATATYPE = Literal["BLOB", "INTEGER", "NUMERIC", "REAL", "TEXT"]

class Column:
    """Represents columns used in SQLite tables.
    
    Attributes:
        name (str): Name of the column.
        datatype (:data:`DATATYPE`): Datatype affinity of the column.
    """
    def __init__(self, name: str, datatype: str):
        self.name = name
        self.datatype = self._datatype_validation(datatype)
            # Will assign if it passes.

    def _datatype_validation(self, datatype) -> DATATYPE:
        """Ensures the supplied datatype affinity is valid."""
        if datatype in get_args(DATATYPE):
            return datatype
        else:
            raise ValueError("The provided datatype is not a valid affinity.")

    @property
    def definition(self) -> str:
        """str: Definition used for creating tables."""
        definition = f'"{self.name}" {self.datatype}'
        return definition

class Table:
    """Represents tables used in SQLite."""
    def __init__(self, name: str, columns: list[Column]):
        self.name = name
        self.columns = columns