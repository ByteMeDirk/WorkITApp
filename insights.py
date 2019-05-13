import matplotlib.pyplot as plt
from scripts import *
import os

teams = get_teams()
users = get_users()
cards = get_cards()
boards = get_boards()
archive = get_archive()


def generate_insights():
    os.remove(r"static/card_labels.png")
    backlog, in_progress, in_review, done, sizes = 0, 0, 0, 0, []
    for card in cards:
        if card['label'] == 'Backlog': backlog += 1
        if card['label'] == 'In Progress': in_progress += 1
        if card['label'] == 'In Review': in_review += 1
        if card['label'] == 'Done': done += 1

    sizes.append(backlog)
    sizes.append(in_progress)
    sizes.append(in_review)
    sizes.append(done)

    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    labels = 'Backlog', 'In Progress', 'In Review', 'Done'
    explode = (0, 0, 0, 0)

    plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.savefig('static/card_labels.png')
    print('Generated card_labels.png')
