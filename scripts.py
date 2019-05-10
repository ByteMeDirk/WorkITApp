import datetime
import sqlite3


def date_time():
    date = datetime.datetime.now()
    return '{}/{}/{}'.format(date.year, date.month, date.day)


def get_teams():
    con_teams = sqlite3.connect("database.db")
    con_teams.row_factory = sqlite3.Row

    cur = con_teams.cursor()
    cur.execute("SELECT * FROM team")

    teams = cur.fetchall()
    con_teams.close()
    return teams


def get_users():
    con_users = sqlite3.connect("database.db")
    con_users.row_factory = sqlite3.Row

    cur = con_users.cursor()
    cur.execute("SELECT * FROM user")

    users = cur.fetchall()
    con_users.close()
    return users
