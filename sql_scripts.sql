
-- первое задание 
UPDATE users SET created_at = NOW() WHERE creaeted_at IS NULL; 
UPDATE users SET tupdated_at = NOW() WHERE tupdated_at IS NULL;

-- второе задание 


-- задание номер 3
SELECT * FROM storehouses_products ORDER BY IF(value=0, 1, 0), value;


