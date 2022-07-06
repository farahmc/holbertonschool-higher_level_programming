-- script that lists all shows without the genre Comedy
-- list by show title in ascending order
SELECT tv_shows.title
       FROM tv_shows
       	    LEFT JOIN tv_show_genres
	    ON tv_shows.id = tv_show_genres.show_id

	    LEFT JOIN tv_genres
	    ON tv_genres.id = tv_show_genres.genre_id
	    WHERE tv_shows.title NOT IN (
	    	  SELECT title
		  	 FROM tv_shows
			      JOIN tv_show_genres
			      ON tv_shows.id = tv_show_genres.show_id

			      JOIN tv_genres
			      ON tv_genres.id = tv_show_genres.genre_id
			      WHERE tv_genres.name = 'Comedy'
			      )

       GROUP BY tv_shows.title
       ORDER BY tv_shows.title ASC;
