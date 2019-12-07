-- БД для сайта https://hd.kinopoisk.ru
DROP DATABASE IF EXISTS kinopoisk_hd;

CREATE DATABASE kinopoisk_hd;

SHOW DATABASES;

USE kinopoisk_hd;

-- Таблица пользователей
CREATE TABLE users (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL UNIQUE,
  phone VARCHAR(12) NOT NULL UNIQUE,
  created_at DATETIME DEFAULT NOW(),
  updated_at DATETIME DEFAULT NOW()
);

-- Таблица профилей 
CREATE TABLE profiles (
	user_id INT UNSIGNED NOT NULL,
	sex char(1) COLLATE utf8_unicode_ci NOT NULL,
	birthday date DEFAULT NULL
);

-- Таблица всех медиафайлов 

CREATE TABLE media (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	media_name VARCHAR(500) NOT NULL,
	country VARCHAR(100) NOT NULL,
	PEGI VARCHAR(50) NOT NULL,
	serial_id INT UNSIGNED,
	created_at DATETIME DEFAULT NOW(),
	poster_id INT UNSIGNED NOT NULL
);

-- Возрастное ограничение PEGI

CREATE TABLE PEGI (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(100) NOT NULL
);

-- Таблица жанров 

CREATE TABLE genre (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL
);

-- Таблица категорий 

CREATE TABLE categoria (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL
);

-- Таблица постеров для фильмов

CREATE TABLE posters (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL
);

-- Таблица Сериалов

CREATE TABLE serials (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL
);

-- Таблица связи многие ко многим фильмы пользователи (приобретенные фильмы)

CREATE TABLE sail_media (
	media_id INT UNSIGNED NOT NULL,
	user_id INT UNSIGNED NOT NULL
);

-- Таблица Рекомендованные категории для пользователей 

CREATE TABLE recommended_categoria (
	categoria_id INT UNSIGNED NOT NULL,
	user_id INT UNSIGNED NOT NULL
);

-- Таблица присвоения жанров фильмам

CREATE TABLE film_genre (
	genre_id INT UNSIGNED NOT NULL,
	media_id INT UNSIGNED NOT NULL
);

-- Таблица присвоения категории фильму

CREATE TABLE film_categoria (
	categoria_id INT UNSIGNED NOT NULL,
	media_id INT UNSIGNED NOT NULL
);


