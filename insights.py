from scripts import *
import matplotlib.pyplot as plt
import os
import collections
import sqlite3

teams = get_teams()
users = get_users()
cards = get_cards()
boards = get_boards()
archive = get_archive()


def daily_card_count():
    print('Updating Daily Card Count')
    conn = sqlite3.connect('database.db')
    today = date_time()
    count = 0
    for card in cards: count += 1

    cur = conn.cursor()
    last_in = cur.execute('SELECT day FROM "card_count" WHERE day=(SELECT MAX(day) FROM "card_count")')
    for last in last_in:
        if last[0] == today:
            print('Updating already existing date')
            cur.execute('UPDATE "card_count" SET count=? WHERE day=?', (count, today))
        else:
            print('Adding a new day')
            cur.execute('INSERT INTO "card_count"(count, day) VALUES (?, ?)', (count, today))

    conn.commit()
    conn.close()


daily_card_count()


def card_list_count():
    result = [0, 0, 0, 0]
    for card in cards:
        if card['label'] == 'Backlog': result[0] += 1
        if card['label'] == 'In Progress': result[1] += 1
        if card['label'] == 'In Review': result[2] += 1
        if card['label'] == 'Done': result[3] += 1
    print('card_list_count: ', result)
    return result


card_list_count()


def board_card_count():
    result = {}
    for board in boards:
        result.update({board['name']: 0})
    for board in boards:
        for card in cards:
            if card['board'] == board['name']: result[board['name']] += 1
    print('board_card_count: ', result)
    return result


board_card_count()


def card_calendar():
    all_dates_keys = []
    all_dates_vals = []

    for card in cards:
        all_dates_keys.append(card['due_date'][:-3])
        all_dates_vals.append(0)

    all_dates_dict = dict(zip(all_dates_keys, all_dates_vals))

    for card in cards:
        for date in all_dates_dict:
            if card['due_date'][:-3] == date: all_dates_dict[card['due_date'][:-3]] += 1

    print('card_calendar: ', all_dates_dict)
    return all_dates_dict


card_calendar()


def carousel_insights():
    boards_list = []
    for card in cards:
        boards_list.append(card['board'])

    return collections.Counter(boards_list)


carousel_insights()


def total_reload():
    daily_card_count()
    card_list_count()
    board_card_count()
    card_calendar()
    carousel_insights()
    get_daily_card_count()
