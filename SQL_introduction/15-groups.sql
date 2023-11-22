-- Script to list the number of records with the same value in a column
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
