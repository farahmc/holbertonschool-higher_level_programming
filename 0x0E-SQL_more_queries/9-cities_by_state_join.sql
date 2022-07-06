-- script that lists all cities contained in the database hbtn_0d_usa
-- list all cities
SELECT cities.id, cities.name, states.name
       FROM cities
       JOIN states
-- these are the columns which match
       ON cities.state_id = states.id
-- order by cities.id in ascending order
       ORDER BY cities.id;
