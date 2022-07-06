-- script that creates the database hbtn_0d_usa and the table states
-- create database, no error if database already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create table, no error if table already exists
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
-- create columns, data type, auto generated unique id, not null, id is primary key
   id 	  INT 	   	NOT NULL AUTO_INCREMENT UNIQUE,
   name   VARCHAR(256) 	NOT NULL,
   PRIMARY KEY (id)
);
