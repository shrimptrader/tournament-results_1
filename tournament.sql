-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE players (id SERIAL PRIMARY KEY, name TEXT);
CREATE TABLE matches (id SERIAL PRIMARY KEY, winner INT, loser INT);

DROP VIEW IF EXISTS tournaments;

-- Creates a view that list all tournaments regardless if there is a winner or loser
CREATE VIEW tournaments AS SELECT players.id, players.name, COUNT(matches.id) AS matches FROM players, matches 
WHERE players.id = matches.winner OR players.id =  matches.loser GROUP BY players.id;

DROP VIEW IF EXISTS standings;

-- Creates standings view by joining tournaments view with matches and players table
CREATE VIEW standings AS SELECT players.id, players.name, COUNT(matches.winner) 
AS wins, COALESCE(tournaments.matches,0) AS matches 
FROM players LEFT JOIN matches
ON players.id = matches.winner
LEFT JOIN tournaments
ON tournaments.id = players.id
GROUP BY matches.winner, players.id, tournaments.matches
ORDER BY wins DESC;
