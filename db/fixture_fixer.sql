DROP TABLE IF EXISTS fixtures;
DROP TABLE IF EXISTS teams;




CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)

);



CREATE TABLE fixtures (
    id SERIAL PRIMARY KEY,
    team1_id SERIAL REFERENCES teams(id) ON DELETE CASCADE,
    team2_id SERIAL REFERENCES teams(id) ON DELETE CASCADE,
    team1_score INT,
    team2_score INT
);
 