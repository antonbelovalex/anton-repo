-- Создание индексов для БД вк
USE vk;
CREATE UNIQUE INDEX users_email_uq ON users(email);

CREATE INDEX users_first_name ON users(first_name);


CREATE INDEX users_last_name ON users(last_name);


CREATE INDEX communities_name ON communities(name);


CREATE INDEX file_name_media ON media(filename) ;



-- Задание на оконные функции

