
-- первое задание 
UPDATE users SET created_at = NOW() WHERE creaeted_at IS NULL; 
UPDATE users SET tupdated_at = NOW() WHERE tupdated_at IS NULL;

-- второе задание 
created_at = DATE_FORMAT(STR_TO_DATE(created_at,'%d.%m.%Y %H:%i'), '%Y-%m-%d %H:%i:00')

-- задание номер 3
SELECT * FROM storehouses_products ORDER BY IF(value=0, 1, 0), value;


