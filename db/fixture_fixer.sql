-- DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS fixtures;
DROP TABLE IF EXISTS teams;
-- DROP TABLE IF EXISTS hometeam;




CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    wins INT,
    losses INT,
    draws INT
);



CREATE TABLE fixtures (
    id SERIAL PRIMARY KEY,
    team1_id SERIAL REFERENCES teams(id) ON DELETE CASCADE,
    team2_id SERIAL REFERENCES teams(id) ON DELETE CASCADE,
    team1_score INT,
    team2_score INT
);
 
--  CREATE TABLE matches (
--      match_id SERIAL PRIMARY KEY,
--      winner INT,
--      loser INT
-- );