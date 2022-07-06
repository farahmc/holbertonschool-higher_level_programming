-- script that lists all the cities of California found in the database hbtn_0d_usa
-- list cities with state_id of California
SELECT id, name
       FROM hbtn_0d_usa.cities
       WHERE state_id = 1
       ORDER BY id;