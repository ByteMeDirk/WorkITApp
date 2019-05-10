# import sqlite3
#
# conn = sqlite3.connect('database.db')
# print("Opened database successfully")
#
# conn.execute('CREATE TABLE team'
#              '(id INTEGER PRIMARY KEY AUTOINCREMENT,'
#              'name TEXT,'
#              'description TEXT)')
#
# print("Table created successfully")
# conn.close()
#
# conn = sqlite3.connect('database.db')
# print("Opened database successfully")
#
# conn.execute('CREATE TABLE board'
#              '(id INTEGER PRIMARY KEY AUTOINCREMENT,'
#              'name TEXT,'
#              'description TEXT,'
#              'privacy TEXT,'
#              'state_list TEXT,'
#              'starred INTEGER)')
#
# print("Table created successfully")
# conn.close()
#
# conn = sqlite3.connect('database.db')
# print("Opened database successfully")
#
# conn.execute('CREATE TABLE card'
#              '(id INTEGER PRIMARY KEY AUTOINCREMENT,'
#              'name TEXT,'
#              'description TEXT,'
#              'state TEXT,'
#              'owner TEXT,'
#              'label TEXT,'
#              'creation_date TEXT,'
#              'due_date TEXT,'
#              'edited_date TEXT,'
#              'comment TEXT,'
#              'creator TEXT,'
#              'current_owner TEXT,'
#              'previous_owner TEXT,'
#              'attachment BLOB)')
#
# print("Table created successfully")
# conn.close()
#
# conn = sqlite3.connect('database.db')
# print("Opened database successfully")
#
# conn.execute('CREATE TABLE user'
#              '(id INTEGER PRIMARY KEY AUTOINCREMENT,'
#              'name TEXT,'
#              'email TEXT,'
#              'title TEXT,'
#              'card TEXT,'
#              'team TEXT,'
#              'profile BLOB)')
#
# print("Table created successfully")
# conn.close()
