-- Compute the max temperature by each state ordered by state
SELECT state, max(value) as max_temp FROM temperatures GROUP BY state order by state;
