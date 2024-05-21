-- script that updates the score of Bob to 10 in the table second_table.
-- You are not allowed to use Bob’s id value, only the name field
-- The database name will be passed as an argument of the mysql command
-- 1)cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
-- 2)cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
UPDATE 
	second_table
SET 
	SCORE = 10
WHERE 
	name = "Bob";

