SELECT manufacturer, COUNT(*) AS num_flights
FROM planes
JOIN flights ON planes.tailnum = flights.tailnum
GROUP BY manufacturer
ORDER BY num_flights DESC
LIMIT 1;

SELECT manufacturer, SUM(air_time) AS total_flying_hours
FROM planes
JOIN flights ON planes.tailnum = flights.tailnum
GROUP BY manufacturer
ORDER BY total_flying_hours DESC
LIMIT 1;

SELECT tailnum, SUM(air_time) AS total_flying_hours
FROM flights
GROUP BY tailnum
ORDER BY total_flying_hours DESC
LIMIT 1;

SELECT dest, AVG(arr_delay) AS avg_delay
FROM flights
GROUP BY dest
ORDER BY avg_delay DESC
LIMIT 1;

SELECT manufacturer, SUM(distance) AS total_distance
FROM planes
JOIN flights ON planes.tailnum = flights.tailnum
GROUP BY manufacturer
ORDER BY total_distance DESC
LIMIT 1;

SELECT origin, COUNT(*) AS num_flights
FROM flights
WHERE DAYOFWEEK(CONCAT(year, '-', month, '-', day)) IN (1, 7) -- Assuming 1 is Sunday and 7 is Saturday
GROUP BY origin
ORDER BY num_flights DESC
LIMIT 1;