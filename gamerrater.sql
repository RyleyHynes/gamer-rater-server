SELECT
    g.title
FROM game g 
JOIN rating r ON g.id = r.game_id