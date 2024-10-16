-- 
    SELECT genres.name AS genre, COUNT(tv_show_genres.tv_show_id) AS number_of_shows
    FROM genres
    LEFT JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
    GROUP BY genres.genre_name
    HAVING COUNT(tv_show_genres.tv_show_id) > 0
    ORDER BY number_of_shows DESC;