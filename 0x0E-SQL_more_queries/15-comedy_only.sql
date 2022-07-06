-- script that lists all Comedy shows in the database hbtn_0d_tvshows
-- list shows by name
SELECT tv_shows.title
       FROM tv_shows
-- first link with tv show genres by show id
       	    JOIN tv_show_genres
	    ON tv_shows.id = tv_show_genres.show_id
-- second link with genre id and show genre id
	    JOIN tv_genres
	    ON tv_genres.id = tv_show_genres.genre_id
-- only list Comedy genre by title in ascending order
       WHERE tv_genres.name = 'Comedy'
       ORDER BY tv_shows.title ASC;
