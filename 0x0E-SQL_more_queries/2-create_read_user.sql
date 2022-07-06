-- script that creates the database hbtn_0d_2 and the user user_0d_2
-- create database, no error if db exists
CREATE DATABASE
       IF NOT EXISTS hbtn_0d_2;
-- create user with password, no error if user exists
CREATE USER
       IF NOT EXISTS 'user_0d_2'@'localhost'
       IDENTIFIED BY 'user_0d_2_pwd';
-- grant SELECT privilege to user on this db
GRANT SELECT on hbtn_0d_2.*
      TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
