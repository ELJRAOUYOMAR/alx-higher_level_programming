-- script that computes the score average of all records in the table second_table
-- The result column name should be average
-- The database name will be passed as an argument of the mysql command
-- cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT 
	AVG(score) AS average
FROM
	second_table

