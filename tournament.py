#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    """Needed to past 1st test, also used in all test
    to delete old matches"""

    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM matches")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    """Needed to past 2nd test, also used in all test
    to delete old players"""

    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM players")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    """Needed to pass 3rd test"""

    conn = connect()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM players")
    pcount = c.fetchall()[0][0]
    conn.close()
    return pcount


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """

    """Needed to pass test# 5,6,7 & 8"""
    conn = connect()
    c = conn.cursor()
    c.execute('INSERT INTO players (name) VALUES (%s)', (name,))
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    """SQL standings view created for test 6 & 7"""

    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM standings;")
    standings = c.fetchall()
    conn.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    """Inserts winner and loser player id's into standings view
    used for test 7 & 8"""

    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO matches (winner,loser) VALUES (%s, %s)",
              (winner, loser))
    conn.commit()
    conn.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    """Creates python list by pairing presorted sql results starting
    at the top and matching with next result"""

    standings = playerStandings()
    return ([(standings[i-1][0], standings[i-1][1], standings[i][0],
            standings[i][1]) for i in range(1, len(standings), 2)])


