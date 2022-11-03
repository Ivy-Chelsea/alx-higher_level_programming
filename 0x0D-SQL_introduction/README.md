# 0x0D-sql_Introduction

Files  | Description
-----  | -----------
[0-list_databases.sql](./0-list_databases.sql)  | A script that lists all databases of my My SQLserver
[1-create_database_if_missing.sql](./1-create_database_if_missing.sql)  | A script that creates the database hbtn_0c_0 in my MySQL server withpout using SELECT or SHOW statements
[2-remove_database.sql](./2-remove_database.sql)  | A script that deletes database hbtn_0c_0 in my MySQL server without using SELECT or SHOW statements.
[3-list_tables.sql](./3-list_tables.sql)  | A script that lists all tables of a databse, the database is passed as an argument of mysql command.
[4-first_table.sql](./4-first_table.sql)  | A script that creates a table first_table
[5-full_table.sql](./5-full_table.sql)  | A script that prints full description of first_table from database hbtn_0c_0 without using DESCRIBE or EXPLAIN statements.
[6-list_values.sql](./6-list_values.sql) | A script that lists all rows of the table first_table from the database hbtn_0c_0 with all field printed
[7-insert_value.sql](./7-insert_value.sql) | A script that inserts a new row in the table first_table
[8-count_89.sql](./8-count_89.sql) | A script that displays number of records with id = 89 in table first_table of database hbtn_0c_0
[9-full_creation.sql](./9-full_creation.sql) | A script that creates table second_table in database hbtn_0c_0 using only SELECT & SHOW statements
[10-top_score.sql](./10-top_score.sql) | A script that lists all records of table second_table of database hbtn_0c_0. Results should display score and name in thsi order.
[11-best_score.sql](./11-best_score.sql) | A script that lists all records with a score >= 10in table second_table of database hbtn_0c_0
[12-no_cheating.sql](./12-no_cheating.sql) | A script that updataes the score of Bob to 10 in table second_table
[13-change_class.sql](./13-change_class.sql) | A script that removes all records with score <= 5in table second_table of database hbtn_0c_0
[14-average.sql](./14-average.sql) | A script that computes the score average of all records in table second_table of database hbtn_0c_0. Result column name should be average
[15-groups.sql](./15-groups.sql) | A script that lists the number of records with the same score in table second_table of database hbtn_0c_0 inndescending order
[16-no_link.sql](./16-no_link.sql) | A script that lists all records of table second_table of database hbtn_0c_0 in descending order. No listing rows without a 'name' value
[100-move_to_utf8.sql](./100-move_to_utf8.sql) | A script that converts hbtn_0c_0 database, first table & field name to UTF8
[101-avg_temperatures.sql](./101-avg_temperatures.sql) | A script that displays the average temperature in farenheight by city ordered by temperature in descending order
[102-top_city.sql](./102-top_city.sql) | A script that displays top 3 of cities temperature during Huly and August by temperature in descending order
[103-max_state.sql](./103-max_state.sql) | A script that displays max temperature of each state ordered by State name
