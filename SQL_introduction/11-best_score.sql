-- list all records with a score >= 10 in second table
SELECT score, TABLE_NAME
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
