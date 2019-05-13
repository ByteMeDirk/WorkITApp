import datetime
import sqlite3


def date_time():
    date = datetime.datetime.now()
    return '{}-{}-{}'.format(date.year, date.month, date.day)


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


def get_boards():
    con_boards = sqlite3.connect("database.db")
    con_boards.row_factory = sqlite3.Row

    cur = con_boards.cursor()
    cur.execute("SELECT * FROM board")

    boards = cur.fetchall()
    con_boards.close()
    return boards


def get_cards():
    con_cards = sqlite3.connect("database.db")
    con_cards.row_factory = sqlite3.Row

    cur = con_cards.cursor()
    cur.execute("SELECT * FROM card")

    cards = cur.fetchall()
    con_cards.close()
    return cards


def get_specific_board(board_name):
    kanban_conn = sqlite3.connect('database.db')
    kanban_conn.row_factory = sqlite3.Row

    cur = kanban_conn.cursor()
    cur.execute("SELECT * FROM board WHERE name='%s'" % board_name)

    board = cur.fetchall()

    kanban_conn.close()
    return board


def get_specific_card(card_name):
    kanban_conn = sqlite3.connect('database.db')
    kanban_conn.row_factory = sqlite3.Row

    cur = kanban_conn.cursor()
    cur.execute("SELECT * FROM card WHERE name='%s'" % card_name)

    board = cur.fetchall()

    kanban_conn.close()
    return board


def get_archive():
    con_cards = sqlite3.connect("database.db")
    con_cards.row_factory = sqlite3.Row

    cur = con_cards.cursor()
    cur.execute("SELECT * FROM card_archive")

    card_arch = cur.fetchall()
    con_cards.close()
    return card_arch
