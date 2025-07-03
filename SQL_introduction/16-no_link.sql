-- lists all records of the table
SELECT sccore, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
