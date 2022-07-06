-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- list genres showing only genre name
SELECT tv_genres.name
       FROM tv_genres
       	    JOIN tv_show_genres
-- first link between genre and genre id
	    ON tv_genres.id = tv_show_genres.genre_id
-- second link between show id and genre show id
	    JOIN tv_shows
       	    ON tv_shows.id = tv_show_genres.show_id
-- for the show Dexter
       WHERE tv_shows.title = 'Dexter'
       ORDER BY tv_genres.name ASC;
