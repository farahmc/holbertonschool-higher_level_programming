-- script that lists all shows contained in hbtn_0d_tvshows with at least 1 linked genre
-- list shows displaying title and genre_id columns
SELECT tv_shows.title, tv_show_genres.genre_id
       FROM tv_shows
       JOIN tv_show_genres
-- this is the linked genre
       ON tv_shows.id = tv_show_genres.show_id
-- order by title and genre_id in ascending order
       ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
