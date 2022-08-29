SELECT
    p.game_id,
    g.id AS game,
    g.title
FROM gamerapi_game g 
LEFT JOIN gamerapi_picture p ON g.id = p.game_id
WHERE p.game_id is null
