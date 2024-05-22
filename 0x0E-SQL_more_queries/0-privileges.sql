-- script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
-- cat 0-privileges.sql | mysql -hlocalhost -uroot -p
--  echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
-- echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
-- cat 0-privileges.sql | mysql -hlocalhost -uroot -p
SHOW GRANTS FOR 'user_0d_2'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
