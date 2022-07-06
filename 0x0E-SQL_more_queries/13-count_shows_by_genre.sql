-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- list shows, displaying in columns genre and number of shows
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
       FROM tv_genres
       JOIN tv_show_genres
       ON tv_genres.id = tv_show_genres.genre_id
-- group by genre
       GROUP BY tv_genres.name
-- order by number of shows linked in descending order
       ORDER BY number_of_shows DESC;
