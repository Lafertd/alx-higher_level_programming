-- Avg temperature in f
SELECT city, AVG(value) AS avg_temp FROM temperatures ORDER BY avg_temp DESC;
