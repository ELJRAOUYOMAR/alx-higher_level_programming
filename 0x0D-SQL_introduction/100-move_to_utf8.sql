-- script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- You need to convert all of the following to UTF8;
-- 1)Database hbtn_0c_0
-- 2)Table first_table
-- 3)Field name in first_table

-- Use the database
USE hbtn_0c_0;

-- Convert the database character set and collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert the table character set and collation
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


