-- order score and condition more than 10 score

SELECT `score`, `name` FROM second_table 
	WHERE `score` >= 10 
	ORDER BY `score` DESC;
