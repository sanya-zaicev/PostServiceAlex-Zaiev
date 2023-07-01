from interface import *
import interface
import datetime
import sqlite3
import json


class Properties:
    database_filename = ''

    def __init__(self, input=dict()):
        self.database_filename = input.get('database_filename')


class PostServiceAPI:
    def __init__(self):
        with open('properties.json', 'r') as openfile:
            self.properties = json.load(openfile, object_hook=Properties)

        db_filename = self.properties.database_filename
        self.conn = sqlite3.connect(db_filename)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
           userid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
           login TEXT UNIQUE NOT NULL,
           password TEXT NOT NULL,
           name TEXT NOT NULL,
           surname TEXT NOT NULL,
           phone TEXT UNIQUE,
           email TEXT UNIQUE,
           birthdate DATE);
        """)

        self.cur.execute("""CREATE TABLE IF NOT EXISTS addresses(
           addressid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
           country TEXT,
           city TEXT,
           street TEXT,
           house TEXT,
           flat TEXT,
           postindex INTEGER NOT NULL,
           commentary TEXT);
        """)

        self.cur.execute("""CREATE TABLE IF NOT EXISTS orders(
           orderid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
           info TEXT NOT NULL,
           description TEXT,
           senderid INTEGER NOT NULL,
           courierid INTEGER NOT NULL,
           addressid INTEGER NOT NULL);
        """)

        self.cur.execute("""CREATE TABLE IF NOT EXISTS orderstatuses(
           id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
           status TEXT NOT NULL UNIQUE);
        """)

        self.cur.execute("""CREATE TABLE IF NOT EXISTS userstatuses(
           id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
           status TEXT NOT NULL UNIQUE);
        """)

        # self.cur.execute(f"""INSERT INTO userstatuses (status) VALUES ('administrator');""")
        # self.cur.execute(f"""INSERT INTO userstatuses (status) VALUES ('courier');""")
        # self.cur.execute(f"""INSERT INTO userstatuses (status) VALUES ('user');""")
        # self.cur.execute(f"""INSERT INTO users (login, password, name, surname, status)
        #   VALUES ('user', 'user', 'noname', 'noname', {3});""")
        # self.cur.execute(f"""INSERT INTO users (login, password, name, surname, email, birthdate, status)
        #   VALUES ('admin4563', '457297301', 'Иван', 'Петров', 'ivanpetrov@mail.ru', '1995-5-12', {1});""")
        # self.cur.execute(f"""INSERT INTO users (login, password, name, surname, phone, birthdate, status)
        #   VALUES ('vasiliyliyliy', 'orlov1990', 'Василий', 'Орлов', '+79993452845', '1990-10-24', {2});""")
        # conn.commit()

    def setup_interface(self):
        interface.Window(self.add_new_user, self.get_all_users, self.get_statuses, self.redact_user)

    def get_all_users(self):
        self.cur.execute('SELECT * FROM users')
        rows = self.cur.fetchall()
        users = []
        for row in rows:
            user = interface.User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            users.append(user)
        return users

    def add_new_user(self, user: User):
        self.cur.execute(
            "INSERT INTO users (login, password, name, surname, phone, email, birthdate, status) VALUES (?,?,?,?,?,?,?,?)",
            (user.login, user.password, user.name, user.surname, user.phone, user.email, user.birthdate,
             user.status))
        self.conn.commit()

    def redact_user(self, user: User):
        print(user)
        self.cur.execute(
            "UPDATE users SET login = ?, password = ?, name = ?, surname = ?, phone = ?, email = ?, birthdate = ?, status = ? WHERE userid == ?",
            (user.login, user.password, user.name, user.surname, user.phone, user.email, user.birthdate,
             user.status, user.id))
        self.conn.commit()

    def get_statuses(self):
        self.cur.execute("SELECT * FROM userstatuses")
        return dict((v, k) for k, v in self.cur.fetchall())


post_service_api = PostServiceAPI()
post_service_api.setup_interface()