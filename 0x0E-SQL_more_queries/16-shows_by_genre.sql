-- script that lists all shows, and all genres linked to that show
-- list all shows
SELECT tv_shows.title, tv_genres.name
       FROM tv_shows
-- first link tv show id to genre show id, if no genre show NULL
       	    LEFT JOIN tv_show_genres
	    ON tv_shows.id = tv_show_genres.show_id
-- second link to genres
	    LEFT JOIN tv_genres
	    on tv_genres.id = tv_show_genres.genre_id
       ORDER BY tv_shows.title, tv_genres.name ASC;
