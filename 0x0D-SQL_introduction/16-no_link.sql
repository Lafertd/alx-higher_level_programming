--- List all records NOT NULL DESC
SELECT `score`, `name` FROM `second_table` WHERE `name` OR `name` IS NOT NULL ORDER BY `score` DESC;
