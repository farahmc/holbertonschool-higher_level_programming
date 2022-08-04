# 0x0F. Python - Object-relational mapping

## Tasks

### Requirements
- Your code should not be executed when imported
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Tasks 0-6:
  - You must use the module `MySQLdb` (`import MySQLdb`)
- Tasks 7-14:
  - You must use the module `SQLAlchemy`
- You are not allowed to use `execute` with `SQLalchemy`

### 0. Get all states
Write a script that lists all states from the database `hbtn_0e_0_usa`:
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
- Results must be sorted in ascending order by `states.id`

### 1. Filter states
Write a script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`:
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
- Results must be sorted in ascending order by `states.id`

### 2. Filter states by user input
Write a script that takes in an argument and displays all values in the states table of `hbtn_0e_0_usa` where `name` matches the argument.
- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name` searched (no argument validation needed)
- You must use `format` to create the SQL query with the user input
- Results must be sorted in ascending order by `states.id`

### 3. SQL Injection...
Once again, write a script that takes in arguments and displays all values in the states table of `hbtn_0e_0_usa` where `name` matches the argument. But this time, write one that is safe from MySQL injections!
- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name` searched (no argument validation needed)
- You must use `format` to create the SQL query with the user input
- Results must be sorted in ascending order by `states.id`

### 4. Cities by states
Write a script that lists all cities from the database `hbtn_0e_4_usa`
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- Results must be sorted in ascending order by `cities.id`
- You can use only `execute()` once


### 5. All cities by state
Write a script that lists all cities from the database `hbtn_0e_4_usa`
- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name` (SQL injection free!)
- Results must be sorted in ascending order by `cities.id`
- You can use only `execute()` once


### 6. First state model
Write a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`:
- `State` class:
  - inherits from `Base`
  - links to the MySQL table `states`
  - class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
  - class attribute `name` that represents a column of a string with maximum 128 characters and can’t be null
- *WARNING*: all classes who inherit from `Base` must be imported before calling `Base.metadata.create_all(engine)`

### 7. All states via SQLAlchemy
Write a script that lists all State objects from the database `hbtn_0e_6_usa`
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must import `State` and `Base` from `model_state` - from `model_state import Base, State`
- Results must be sorted in ascending order by `states.id`


### 8. First state
Write a script that prints the first `State` objects from the database `hbtn_0e_6_usa`
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must import `State` and `Base` from `model_state` - from `model_state import Base, State`
- The state you display must be the first in `states.id`
- You are not allowed to fetch all states from the database before displaying the result
- If the table `states` is empty, print `Nothing` followed by a new line


### 9. Contains "a"
Write a script that lists all State objects that contain the letter `a` from the database `hbtn_0e_6_usa`
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Results must be sorted in ascending order by `states.id`


### 10. Get a state
Write a script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`
- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name to search` (SQL injection free)
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- You can assume you have one record with the state name to search
- Results must display the `states.id`
- If no state has the name you searched for, display `Not found`


### 11. Add a new state
Write a script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Print the new `states.id` after creation


### 12. Update a state
Write a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Change the name of the `State` where `id = 2` to `New Mexico`


### 13. Delete states
Write a script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`


### 14. Cities in state
Write a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City`.
- C`ity` class:
  - inherits from `Base` (imported from `model_state`)
  - links to the MySQL table `cities`
  - class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
  - class attribute `name` that represents a column of a string of 128 characters and can’t be null
  - class attribute `state_id` that represents a column of an integer, can’t be null and is a foreign key to `states.id`
Next, write a script `14-model_city_fetch_by_state.py` that prints all `City` objects from the database `hbtn_0e_14_usa`:
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `cities.id`
- Results must be displayed: (`<state name>`): (`<city id>`) `<city name>`)
