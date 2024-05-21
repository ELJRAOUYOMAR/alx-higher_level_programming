# SQL Introduction Project

## General Information

This project introduces the fundamental concepts of SQL and relational databases, focusing on MySQL. It covers a variety of essential topics, including:

- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What do DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE, or DELETE data
- What are subqueries
- How to use MySQL functions

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e., syntax above)
- All your files should start with a comment describing the task
- All SQL keywords should be in uppercase (e.g., `SELECT`, `WHERE`)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## More Information

### Comments for Your SQL Files

Example of how to comment your SQL queries:

```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;

```

## Installing MySQL 8.0 on Ubuntu 20.04 LTS

To install MySQL 8.0 on Ubuntu 20.04 LTS, follow these steps:

```terminal
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```

## Connecting to Your MySQL Server

To connect to your MySQL server, use the following command:

```terminal
To connect to your MySQL server, use the following command:
```

Example session:

```terminal
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> quit
Bye
```

## Using “Container-on-Demand” to Run MySQL

In the container, credentials are root/root.

Steps:
1. Ask for a container with Ubuntu 20.04.
2. Connect via SSH or the Web terminal.
3. Start MySQL in the container:
```
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
```
4. Execute SQL scripts in the container:
```
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys      
```
In the container, use the credentials root/root.

---

This README provides an overview of the SQL Introduction project, detailing the essential topics covered, requirements, and steps to set up and use MySQL on Ubuntu 20.04 LTS. This project is designed to familiarize you with SQL and relational databases, providing a foundation for more advanced database management tasks.


