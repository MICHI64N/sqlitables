# Reference
## Functions
### `connection.connect(file_path)`
Connects to the database
* **Parameters**
    * `file_path`: *string*; The file path to the database (or its desired location)
* **Returns**
    * `connection`: *sqlite3.Connection*; The database connection
    * `cursor`: *sqlite3.Cursor*; The cursor to navigate the database with

## Classes
### `classes.Column`
#### `__init__(self, name, datatype)`
* **Parameters**
    * `name`: *string*; The name of the column
    * `datatype`: *string*; The datatype of the column
* **Returns**
    * `self.name`: *string*; instance "name" attribute
    * `self.datatype` *string*; instance "datatype" attribute

#### `statement(self)`
Creates a statement that can be applied to the creation of tables
* **Parameters**: *There are no parameters for this function*
* **Returns**
    * `statement`: *string*; a statement that can be applied to the creation of tables

### `classes.Table`
#### `__init__(self, name, columns)`
* **Parameters**
    * `name`: *string*; The name of the table
    * `columns`: *list\[classes.Column\]*; The columns to apply to the table
* **Returns**
    * `self.name`: *string*; instance "name" attribute
    * `self.columns`: *list\[classes.Column\]*; instance "columns" attribute

#### `exists(self, cursor)`
Checks whether the table exists in the database
* **Parameters**
    * `cursor`: *sqlite3.Cursor*; The cursor to navigate the database with
* **Returns**
    * `exists`: *boolean*; The answer to whether the table exists in the database

#### `create(self, cursor)`
Creates the table in the database
* **Parameters**
    * `cursor`: *sqlite3.Cursor*; The cursor to navigate the database with
* **Returns**: *This function does not return*