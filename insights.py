from scripts import *
import matplotlib.pyplot as plt
import os

teams = get_teams()
users = get_users()
cards = get_cards()
boards = get_boards()
archive = get_archive()


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
