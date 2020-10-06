DROP TABLE IF EXISTS fixtures;
DROP TABLE IF EXISTS teams;


CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE fixtures (
    fixture_id SERIAL PRIMARY KEY,
    team1_id SERIAL REFERENCES teams(id),
    team2_id SERIAL REFERENCES teams(id)
);
