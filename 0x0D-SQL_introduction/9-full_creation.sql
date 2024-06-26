-- script that creates a table second_table
-- The database name will be passed as an argument to the mysql command
-- If the table second_table already exists, your script should not fail
-- You are not allowed to use the SELECT and SHOW statements
-- cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
CREATE TABLE
	IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);

INSERT INTO 
	second_table 
VALUES
    (1, "John", 10),
    (2, "Alex", 3),
    (3, "Bob", 14),
    (4, "George", 8);
