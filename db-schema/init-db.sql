CREATE DATABASE IF NOT EXISTS basicwebapi;
USE basicwebapi;

DROP TABLE IF EXISTS songs;

CREATE TABLE songs (
	id INTEGER auto_increment NOT NULL,
	title VARCHAR(100) NOT NULL,
	artist VARCHAR(100) NOT NULL,
	duration INTEGER NOT NULL,
	uploadDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	CONSTRAINT songs_PK PRIMARY KEY (id),
	CONSTRAINT songs_UN UNIQUE KEY (title)
);


CREATE DATABASE IF NOT EXISTS `basicwebapi-test`;
USE `basicwebapi-test`;

DROP TABLE IF EXISTS songs;

CREATE TABLE songs (
	id INTEGER auto_increment NOT NULL,
	title VARCHAR(100) NOT NULL,
	artist VARCHAR(100) NOT NULL,
	duration INTEGER NOT NULL,
	uploadDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	CONSTRAINT songs_PK PRIMARY KEY (id),
	CONSTRAINT songs_UN UNIQUE KEY (title)
);

INSERT INTO songs (title, artist, duration)
VALUES
  ('Motteke! Sailor Fuku!', 'Lucky Star', 267);