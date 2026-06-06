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
    * `self.name`: *string*; Instance "name" attribute
    * `self.datatype` *string*; Instance "datatype" attribute
    * `self.constraints` *list*; Instance "constraints" attribute (empty list by default)

#### `constraints(self, constraint, value)`
Adds a constraint to the instances's self.constraints attribute.
* **Parameters**:
    * `constraint`: *string*; A constraint to apply (only accepts "CHECK", "COLLATE", "DEFAULT", "PRIMARY KEY", "NOT NULL", and "UNIQUE" case-insensitive)
    * `value`: *string, integer, None*; A value to apply to the constraint
* **Returns**
    * `self.constraints`: *list[string]*; Updated instance "constraints" attribute

#### `definition(self)`
Creates a definition that can be applied to the creation of tables
* **Parameters**: *There are no parameters for this function*
* **Returns**
    * `definition`: *string*; A definition that can be applied to the creation of tables

### `classes.Table`
#### `__init__(self, name, columns)`
* **Parameters**
    * `name`: *string*; The name of the table
    * `columns`: *list\[classes.Column\]*; The columns to apply to the table
* **Returns**
    * `self.name`: *string*; Instance "name" attribute
    * `self.columns`: *list\[classes.Column\]*; Instance "columns" attribute

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

#### `insert(self, values, connection)`
Inserts values into the table
* **Parameters**
    * `values`: *list\[tuple\]*; The values to insert into the table
    * `connection`: *sqlite3.Connection*; The connection to the database
* **Returns**: *This function does not return*

#### `select(self, select, where, cursor)`
Selects values from the table
* **Parameters**
    * `select`: *list[classes.Column], string*; The columns to select from (the only string value accepted is "\*")
    * `where`: *string, none*; The where clause filtering which values to select
    * `cursor`: *sqlite3.Cursor*; The cursor to navigate the database with
* **Returns**
    * `selection`: *list*; The selected values