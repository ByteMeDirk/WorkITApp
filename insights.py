from scripts import *
import matplotlib.pyplot as plt

teams = get_teams()
users = get_users()
cards = get_cards()
boards = get_boards()
archive = get_archive()


def card_list_pie_plot():
    backl, inpro, inrev, done, sizes = 0, 0, 0, 0, []
    labels = 'Backlog', 'In Progress', 'In Review', 'Done'
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    for card in cards:
        if card['label'] == 'Backlog': backl += 1
        if card['label'] == 'In Progress': inpro += 1
        if card['label'] == 'In Review': inrev += 1
        if card['label'] == 'Done': done += 1

    sizes.append(backl)
    sizes.append(inpro)
    sizes.append(inrev)
    sizes.append(done)

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    return plt
