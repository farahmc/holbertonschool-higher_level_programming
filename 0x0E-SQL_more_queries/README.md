# SQL - More Queries

## Tasks

### 0. My privileges!
Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`)

### 1. Root user
Write a script that creates the MySQL server user `user_0d_1`.
- `user_0d_1` should have all privileges on your MySQL server
- The `user_0d_1` password should be set to `user_0d_1_pwd`
- If the user `user_0d_1` already exists, your script should not fail

### 2. Read user
Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`.
- `user_0d_2` should have only `SELECT` privilege in the database `hbtn_0d_2`
- The `user_0d_2` password should be set to `user_0d_2_pwd`
- If the database `hbtn_0d_2` already exists, your script should not fail
- If the user `user_0d_2` already exists, your script should not fail

### 3. Always a name
Write a script that creates the table `force_name` on your MySQL server.

### 4. ID can't be null
Write a script that creates the table `id_not_null` on your MySQL server.

### 5. Unique ID
Write a script that creates the table `unique_id` on your MySQL server.

### 6. States table
Write a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server.

### 7. Cities table
Write a script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server.

### 8. Cities of California
Write a script that lists all the cities of `California` that can be found in the database `hbtn_0d_usa`.

### 9. Cities by States
Write a script that lists all cities contained in the database `hbtn_0d_usa`.

### 10. Genre ID by show
Write a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.

### 11. Genre ID for all shows
Write a script that lists all shows contained in the database `hbtn_0d_tvshows`.

### 12. No genre
Write a script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.

### 13. Number of shows by genre
Write a script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.

### 14. My genres
Write a script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`.

### 15. Only Comedy
Write a script that lists all Comedy shows in the database `hbtn_0d_tvshows`.

### 16. List shows and genres
Write a script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.

## Advanced Tasks

### 17. Not my genre
Write a script that uses the `hbtn_0d_tvshows` database to list all genres not linked to the show `Dexter`

### 18. No Comedy tonight!
Write a script that lists all shows without the genre `Comedy`

### 19. Rotten tomatoes
Write a script that lists all shows from `hbtn_0d_tvshows_rate` by their rating

### 20. Best genre
Write a script that lists all genres in the database `hbtn_0d_tvshows_rate` by their rating