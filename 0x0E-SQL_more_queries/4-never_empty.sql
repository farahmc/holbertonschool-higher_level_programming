-- script that creates the table id_not_null
-- create a table, no error if it already exists
CREATE TABLE IF NOT EXISTS id_not_null (
-- columns, data type, set default value of id to 1
       id INT DEFAULT 1,
       name VARCHAR(256)
);
