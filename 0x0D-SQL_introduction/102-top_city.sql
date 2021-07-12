-- display top 3 temperature

SELECT `city`, AVG(`value`) AS `avg_temp`
FROM temperatures
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
