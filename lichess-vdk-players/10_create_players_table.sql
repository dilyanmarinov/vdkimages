CREATE TABLE players (
	user_id serial PRIMARY KEY,
	username VARCHAR ( 255 ) UNIQUE NOT NULL)