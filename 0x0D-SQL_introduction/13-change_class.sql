-- script that removes all records with a score <= 5 in the table second_table
-- The database name will be passed as an argument of the mysql command
-- 1) cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
-- 2) cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
DELETE FROM 
	second_table
WHERE 
	score <= 5;
