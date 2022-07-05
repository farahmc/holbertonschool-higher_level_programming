-- script that lists all records of the table second_table of the database hbtn_0c_0
-- no rows without a name value, display score and name by descending score
SELECT score, name
       FROM second_table
       WHERE name IS NOT NULL
       ORDER BY score DESC;
