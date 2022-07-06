-- script that creates the MySQL server user user_0d_1
-- all privileges, set password. script should not fail if user exists
CREATE USER
       IF NOT EXISTS 'user_0d_1'@'localhost'
       IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES on *.* 
       TO 'user_0d_1'@'localhost'
       WITH GRANT OPTION;
FLUSH PRIVILEGES;
