# Usage

## Connect to the Database
### Prerequisites
* None
### Usage
1. Import the required module
    ```py
    from sqlitables import connection
    ```
2. Connect to the database using [connection.connect()](https://github.com/MICHI64N/sqlitables/blob/main/docs/reference.md#connectionconnectfile_path) using a file path compatible with your system. The connection and associated cursor are required for many of the features in the library. A database is created at the file path if it does not already exist.
    ```py
    connection, cursor = connection.connect("/Users/foo/Documents/example.db")
    ```

## Create a Table in the Database
### Prerequisites
* [Connect to the database](https://github.com/MICHI64N/sqlitables/blob/main/docs/usage.md#connect-to-the-database)
### Usage
1. Import the required module
    ```py
    from sqlitables import classes
    ```
2. Create [classes.Column](https://github.com/MICHI64N/sqlitables/blob/main/docs/reference.md#classescolumn) objects by filling their name, datatype, and (optionally) constraints; these columns will be used in the [classes.Table](https://github.com/MICHI64N/sqlitables/blob/main/docs/reference.md#classestable) object.
    ```py
    example_col = classes.Column("Example1", "TEXT", None)
    example_col_2 = classes.Column("Example2", "TEXT", None)
    example_col_3 = classes.Column("Example3", "TEXT", None)
    ```
3. Create the [classes.Table](https://github.com/MICHI64N/sqlitables/blob/main/docs/reference.md#classestable) object—note that the table is not on the database at this point.
    ```py
    example_table_cols = [example_col, example_col_2, example_col_3]
    example_table = classes.Table("Example", example_table_cols)
    ```
4. *Optional*: check if the table exists on the database using [classes.Table.exists()](https://github.com/MICHI64N/sqlitables/blob/main/docs/reference.md#existsself-cursor).
    ```py
    exists = example_table.exists(cursor)
    print(exists)
    ```
5. Create the table on the database if it does not already exist using [classes.Table.create()](https://github.com/MICHI64N/sqlitables/blob/main/docs/reference.md#createself-cursor).
    ```py
    example_table.create(cursor)
    ```

## Insert Values Into a Table
### Prerequisites
* [Connect to the database](https://github.com/MICHI64N/sqlitables/blob/main/docs/usage.md#connect-to-the-database)
* [Create a table in the database](https://github.com/MICHI64N/sqlitables/blob/main/docs/usage.md#create-a-table-in-the-database)
### Usage
1. Insert the values using [classes.Table.insert()](https://github.com/MICHI64N/sqlitables/blob/main/docs/reference.md#insertself-values-connection) according to the number, data type, and constraints of the table's columns. One tuple is one row.
    ```py
    example_table.insert([('Field1','Field2','Field3'), ('Field4','Field5','Field6')], connection)
    ```

## Select Values From a Table
### Prerequisites
* [Connect to the database](https://github.com/MICHI64N/sqlitables/blob/main/docs/usage.md#connect-to-the-database)
* [Create a table in the database](https://github.com/MICHI64N/sqlitables/blob/main/docs/usage.md#create-a-table-in-the-database)
* [Insert Values Into a Table](https://github.com/MICHI64N/sqlitables/blob/main/docs/usage.md#insert-values-into-a-table)
### Usage
1. Select the values using [classes.Table.select()](https://github.com/MICHI64N/sqlitables/blob/main/docs/reference.md#selectself-select-where-cursor) by specifying the columns to select from. To select all columns, use "\*". Optionally, a where clause can be used to filter the selected values. Save this with a variable for the next step.
    ```py
    selection = example_table.select([Example1, Example2], None, cursor)
    ```
2. Print the results to view the selection.
    ```py
    print selection
    ```