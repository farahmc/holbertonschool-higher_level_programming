-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked
-- list shows, showing title and genre id
SELECT tv_shows.title, tv_show_genres.genre_id
       FROM tv_shows
       LEFT JOIN tv_show_genres
       ON tv_shows.id = tv_show_genres.show_id
-- only where no genre is linked
       WHERE tv_show_genres.show_id IS NULL
       ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
