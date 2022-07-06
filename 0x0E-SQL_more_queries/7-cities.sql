-- script that creates the database hbtn_0d_usa and the table cities
-- create database, no error if already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create table, no error if already exists
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
-- create columns, id must be unique, auto-generated, not null
   id	  	   INT	      NOT NULL   AUTO_INCREMENT UNIQUE,
   state_id	   INT	      NOT NULL,
   name		   VARCHAR(26)NOT NULL,
-- primary key is ID
   PRIMARY KEY (id),
-- state_id is foreign key that references id in the states table
   FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
