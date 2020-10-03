DROP TABLE teams;
DROP TABLE users
DROP TABLE fixtures

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE teams (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(255)
);

CREATE TABLE fixtures (
    fixture_id SERIAL PRIMARY KEY,
    hometeam INT,
    awayteam INT

);
