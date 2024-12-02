-- Avg temperature in f
SELECT city, AVG(value) as avg_temp FROM temperatures ORDER BY value DESC;
