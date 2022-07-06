-- script that creates the table unique_id
-- create table, no error if table exists
CREATE TABLE IF NOT EXISTS unique_id (
-- columns, data type, id must have default value and be unique
   id INT DEFAULT 1 UNIQUE,
   name VARCHAR(256)
);
