-- list all cities in database

SELECT `id`, `name`
FROM `cities`
WHERE state_id = (
	SELECT ID
	FROM `states`
	WHERE name = 'California'
);
