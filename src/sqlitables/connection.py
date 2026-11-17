"""Database connection utility."""

import sqlite3

def connect(file_path):
    """Provides a database connection.
    
    Args:
        file_path (:term:`python:path-like object`): Path to the file the database is hosted at.

    Returns:
        :class:`python:sqlite3.Connection`: Connection to the database.

    Note:
        The database is created at the file path if it does not exist.
    """
    connection = sqlite3.connect(file_path)
    return connection