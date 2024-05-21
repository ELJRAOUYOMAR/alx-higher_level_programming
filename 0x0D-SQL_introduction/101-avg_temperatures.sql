-- Import in hbtn_0c_0 database this table dump: 
-- download(https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql)
-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;


