#  0x0E-SQL_more_queries

File | Description
---- | -----------
[0-priviledges.sql](./0-priviledges.sql) | A script that lists all priviledges of users user_0d_1 & user_0d_2 in localhost server)
[1-create_user.sql](./1-create_user.sql) | A script that creates user user_0d_1 having all priviledges and password user_0d_1_pwd
[2-create_read_user.sql](./2-create_read_user.sql) | A script that creates database hbtn_0d_2 & user user_0d_2 with SELECT priviledge & password set to user_0d_2_pwd
[3-force_name.sql](./3-force_name.sql) | A script that creates table force_name
[4-never_empty.sql](./4-never_empty.sql) | Script that creates table id_not_null
[5-unique_id.sql](./5-unique_id.sql) | Script that creates table unique_id
[6-states.sql](./6-states.sql) | Script that creates database hbtn_0d_usa & table states
[7-cities.sql](./7-cities.sql) | Script that creates database hbtn_0d_usa and table cities
[8-cities_of_california_subquery.sql](./8-cities_of_california_subquery.sql) | A script that lists all cities in California that can be found in the database hbtn_0d_usa. Results to be in ascending order and table state contains one record where bane = California
[9-cities_by_state_join.sql](./9-cities_by_state_join.sql) | Script listing all cities contained in the database hbtn_0d_usa. Results to be sorted in ascending order by cities.id and records should display: cities.id - cities.name - states.name
[10-genre_id_by_show.sql](./10-genre_id_by_show.sql) | Script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked. Only SELECT statement can be used
[11-genre_id_all_shows.sql](./11-genre_id_all_shows.sql) | Script that lists all shows contained in the database hbtn_0d_tvshows. If a show doesn't have a genre NULL should be displayed
[12-no_genre.sql](./12-no_genre.sql) | A script that lists all shows contained in hbtn_0d_tvshows without a genre linked
[14-my_genres.sql](./14-my_genres.sql) | A script that uses the hbtn_0d_tvshows database to list all genres of the show Dexter
[15-comedy_only.sql](./15-comedy_only.sql) | A script that lists all Comedy shows in the database hbtn_0d_tvshows. tv_genres table contains only one record where name = Comedy
[16-shows_by_genre.sql](./16-shows_by_genre.sql) | A script that lists all shows & bgenres linked to that show from database hbtn_0d_tvshows
[100-not_my_genres.sql](./100-not_my_genres.sql) | A script that uses hbtn_0d_tvshows databases to list all genres not linked to the show Dexter
[101-not_a_comedy.sql](./101-not_a_comedy.sql) | A script that lists all shows without the gente Comedy in the database hbtn_0d_tvshows. Each record should display: tv_shows.title
[102-rating_shows.sql](./102-rating_shows.sql) | A script that list all shows from hbtn_0d_tvshows by their rating
[103-rating_genres.sql](./103-rating_genres.sql) | A script that lists all genres in the database hbtn_0d_tvshows_rate by their rating using only the SELECT statement
