from flask import Flask, render_template, request
import sqlite3
from flask import Flask
from scripts import *

app = Flask(__name__)
conn = sqlite3.connect('database.db')


@app.route('/')
def base():
    return render_template('base.html', date=date_time())


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_user')
def create_user():
    teams = get_teams()
    return render_template('create_user.html', teams=teams)


@app.route('/create_team')
def create_team():
    return render_template('create_team.html')


@app.route('/create_board')
def create_board():
    return render_template('create_board.html')


@app.route('/user_list')
def user_list():
    users = get_users()
    teams = get_teams()
    return render_template('user_list.html', users=users, teams=teams)


@app.route('/team_list')
def team_list():
    users = get_users()
    teams = get_teams()
    return render_template('team_list.html', users=users, teams=teams)


@app.route('/board_list')
def board_list():
    boards = get_boards()
    return render_template('board_list.html', boards=boards)


@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    user_conn = sqlite3.connect('database.db')
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form.get('email')
            title = request.form.get('title')
            team = request.form.get('team')

            cur = user_conn.cursor()
            cur.execute('INSERT INTO "user"(name, email, title, team) VALUES (?, ?, ?, ?)',
                        (name, email, title, team))

            user_conn.commit()
            msg = "{} added to the system".format(name)
        except:
            user_conn.rollback()
            msg = "Error in insert operation"
        finally:
            user_conn.close()
            return render_template('result.html', msg=msg)


@app.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    user_del_conn = sqlite3.connect('database.db')
    if request.method == 'POST':
        try:
            cur = user_del_conn.cursor()
            cur.execute("DELETE FROM user WHERE name='%s'" % request.form['username'])
            user_del_conn.commit()
            msg = "{} deleted from the system".format(request.form['username'])
        except:
            user_del_conn.rollback()
            msg = "Could not delete {}".format(request.form['username'])
        finally:
            user_del_conn.close()
            return render_template('result.html', msg=msg)


@app.route('/add_team', methods=['POST', 'GET'])
def add_team():
    team_conn = sqlite3.connect('database.db')
    if request.method == 'POST':
        try:
            name = request.form['name']
            description = request.form.get('description')

            cur = team_conn.cursor()
            cur.execute('INSERT INTO "team"(name, description) VALUES (?, ?)',
                        (name, description))

            team_conn.commit()
            msg = "{} added to the system".format(name)
        except:
            team_conn.rollback()
            msg = "Error in insert operation"
        finally:
            team_conn.close()
            return render_template('result.html', msg=msg)


@app.route('/delete_team', methods=['GET', 'POST'])
def delete_team():
    user_del_conn = sqlite3.connect('database.db')
    if request.method == 'POST':
        try:
            cur = user_del_conn.cursor()
            cur.execute("DELETE FROM team WHERE name='%s'" % request.form['teamname'])
            user_del_conn.commit()
            msg = "{} deleted from the system".format(request.form['teamname'])
        except:
            user_del_conn.rollback()
            msg = "Could not delete {}".format(request.form['teamname'])
        finally:
            user_del_conn.close()
            return render_template('result.html', msg=msg)


@app.route('/add_board', methods=['POST', 'GET'])
def add_board():
    board_conn = sqlite3.connect('database.db')
    if request.method == 'POST':
        try:
            name = request.form['name']
            description = request.form['description']
            privacy = request.form['privacy']
            starred = request.form['starred']
            state = request.form['state']

            print(name, description, privacy, starred, state)

            cur = board_conn.cursor()
            cur.execute('INSERT INTO "board"(name, description, privacy, starred, state_list) '
                        'VALUES (?, ?, ?, ?, ?)',
                        (name, description, privacy, starred, state))

            board_conn.commit()
            msg = "{} added to the system".format(name)
        except:
            board_conn.rollback()
            msg = "Error in insert operation"
        finally:
            board_conn.close()
        return render_template('result.html', msg=msg)


@app.route('/delete_board', methods=['GET', 'POST'])
def delete_board():
    board_del_conn = sqlite3.connect('database.db')
    if request.method == 'POST':
        try:
            cur = board_del_conn.cursor()
            cur.execute("DELETE FROM board WHERE name='%s'" % request.form['name'])
            board_del_conn.commit()
            msg = "{} deleted from the system".format(request.form['name'])
        except:
            board_del_conn.rollback()
            msg = "Could not delete {}".format(request.form['name'])
        finally:
            board_del_conn.close()
            return render_template('result.html', msg=msg)


@app.route('/goto_kanban', methods=['GET', 'POST'])
def goto_kanban():
    if request.method == 'POST':
        board_name = request.form['board_name']
        board = get_specific_board(board_name)
        return render_template('kanban.html', board_name=board_name, specific_board=board)


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(debug=True)
