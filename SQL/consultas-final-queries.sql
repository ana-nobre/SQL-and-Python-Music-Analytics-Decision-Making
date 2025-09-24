-- Consultas: 

/* 1. ¿Cuál es el artista con más albums? */

SELECT nombre_artista, COUNT(album) AS total_album_registros
FROM tabla_artista
GROUP BY nombre_artista
ORDER BY total_album_registros DESC
LIMIT 1;

-- Top 5 albums

SELECT nombre_artista, COUNT(album) AS total_album_registros
FROM tabla_artista
GROUP BY nombre_artista
ORDER BY total_album_registros DESC
LIMIT 5;

/* 2. ¿Qué género es el mejor valorado? */ -- (Género con más reproducciones totales)

SELECT s.id_genero, g.genero, SUM(s.reproducciones) AS total_reproducciones
FROM Tabla_stats AS s
INNER JOIN Tabla_genero AS g 
ON s.id_genero = g.id_genero
GROUP BY s.id_genero
ORDER BY total_reproducciones DESC
LIMIT 1;

-- Género con más oyentes

SELECT g.genero, SUM(s.oyentes) AS total_oyentes
FROM Tabla_stats s
JOIN Tabla_genero g 
ON s.id_genero = g.id_genero
GROUP BY s.id_genero
ORDER BY total_oyentes DESC
LIMIT 1;

/* 3. ¿En qué año se lanzaron más álbumes? */

SELECT YEAR(fecha) AS lanzamiento, COUNT(DISTINCT album) AS total_albumes
FROM tabla_tracks
WHERE fecha IS NOT NULL
GROUP BY lanzamiento
ORDER BY total_albumes DESC
LIMIT 1;

/* 4. ¿Cuál es la canción mejor valorada? */

SELECT t.track, t.nombre_artista, SUM(s.reproducciones) AS total_reproducciones
FROM tabla_tracks AS t
JOIN tabla_stats AS s 
ON t.id_artista = s.id_artista
GROUP BY t.track, t.nombre_artista
ORDER BY total_reproducciones DESC
LIMIT 1;

-- TOP 5

SELECT t.track, t.nombre_artista, SUM(s.reproducciones) AS total_reproducciones
FROM tabla_tracks AS t
JOIN tabla_stats AS s 
ON t.id_artista = s.id_artista
GROUP BY t.track, t.nombre_artista
ORDER BY total_reproducciones DESC
LIMIT 5;

/* 5. ¿Cuál es el artista con más valoración? */ -- artista con más reproducciones

SELECT nombre_artista, reproducciones
FROM tabla_stats
ORDER BY reproducciones DESC
LIMIT 1;

-- top 5

SELECT nombre_artista, reproducciones
FROM tabla_stats
ORDER BY reproducciones DESC
LIMIT 5;

/* 6. ¿Cuál es el album más valorado de los años pares de mi selección? */ -- reproducciones por album -- CREO q está mal

SELECT t.album, t.nombre_artista, YEAR(t.fecha) AS año, SUM(s.reproducciones) AS reproducciones_totales
FROM tabla_tracks AS t
JOIN tabla_stats AS s 
    ON t.id_artista = s.id_artista
WHERE YEAR(t.fecha) % 2 = 0
GROUP BY t.album, t.nombre_artista, YEAR(t.fecha)
ORDER BY reproducciones_totales DESC
LIMIT 5;

/* 7. ¿Qué país tiene más artistas? (ordenar por popularidad) */ -- NO TENEMOS COUNTRY

/* 8. ¿Qué artista estuvo más tiempo y cuántos albums tiene? */ -- CREO QUE ESTÁ MAL:

SELECT nombre_artista, COUNT(DISTINCT album) AS total_albums, (MAX(YEAR(fecha)) - MIN(YEAR(fecha)) + 1) AS anios_activo
FROM tabla_tracks
WHERE fecha IS NOT NULL
GROUP BY nombre_artista
ORDER BY anios_activo DESC, total_albums DESC
LIMIT 1;

SELECT nombre_artista, COUNT(DISTINCT album) AS total_albums, (MAX(YEAR(fecha)) - MIN(YEAR(fecha)) + 1) AS anios_activo
FROM tabla_tracks
WHERE fecha IS NOT NULL
GROUP BY nombre_artista
ORDER BY anios_activo DESC, total_albums DESC
LIMIT 5;