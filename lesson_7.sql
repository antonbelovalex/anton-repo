SELECT usrs.first_name, users.last_name, orders.id FROM users 
JOIN orders
ON users.id = orders.user_id;



SELECT products.id, catalogs.id FROM products
JOIN catalogs
ON products.id = catalogs.id;




