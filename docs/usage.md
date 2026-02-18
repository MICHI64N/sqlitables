# Usage
## Create a Table in the Database
1. Import the required modules
    ```py
    from sqlitables import classes, connection
    ```
2. Connect to the database using [connection.connect()](https://github.com/MICHI64N/sqlitables/blob/main/docs/reference.md#connectionconnectfile_path) using a file path compatible with your system. The connection and associated cursor are required for many of the features in the library.
    ```py
    connection, cursor = connection.connect("/Users/foo/Documents/example.db")
    ```
3. Create [classes.Column](https://github.com/MICHI64N/sqlitables/blob/main/docs/reference.md#classescolumn) objects; these columns will be used in the [classes.Table](https://github.com/MICHI64N/sqlitables/blob/main/docs/reference.md#classestable) object.
    ```py
    example_col = classes.Column("Example", "TEXT")
    example_col_2 = classes.Column("Example2", "TEXT")
    example_col_3 = classes.Column("Example3", "TEXT")
    ```
4. Create the [classes.Table](https://github.com/MICHI64N/sqlitables/blob/main/docs/reference.md#classestable) object—note that the table is not on the database at this point.
    ```py
    example_table_cols = [example_col, example_col_2, example_col_3]
    example_table = classes.Table("Example", example_table_cols)
    ```
5. *Optional*: check if the table exists on the database using [classes.Table.exists()](https://github.com/MICHI64N/sqlitables/blob/main/docs/reference.md#existsself-cursor).
    ```py
    exists = example_table.exists(cursor)
    print(exists)
    ```
6. Create the table on the database if it does not already exist using [classes.Table.create()](https://github.com/MICHI64N/sqlitables/blob/main/docs/reference.md#createself-cursor).
    ```py
    example_table.create(cursor)
    ```