-- script that creates the table force_name
-- create the table, no error if table exists
CREATE TABLE IF NOT EXISTS force_name (
-- column, datatype, if value should be null or not null
       id INT,
       name VARCHAR(256) NOT NULL
);
