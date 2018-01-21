from flask import Flask, request
import sqlite3
import json
from passlib.hash import sha256_crypt
from datetime import datetime


def current_time():
    return str(datetime.now())


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn = sqlite3.connect('kmvOnline.db')
conn.row_factory = dict_factory
app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Endpoints:</h1><br>/notifications<br>/add-notification"


@app.route("/notifications")
def all_notifications():
    cursor = conn.cursor()
    cursor.execute(
        '''SELECT title, body, date, name AS teacher FROM collegeNotifications,teachersInfo WHERE teacher = teacherid ORDER BY date DESC ;''')
    return json.dumps({"notifications": cursor.fetchall()})


@app.route("/add-notification", methods=['GET', 'POST'])
def add_notification():
    if request.method == "POST":
        username = request.form.get("username")
        password_candidate = request.form.get("password")
        teacher_id = request.form.get("teacher")
        cursor = conn.cursor()
        cursor.execute(
            '''SELECT * FROM teachersInfo WHERE username = ? AND teacherid = ?;''', (username, teacher_id)
        )
        teacher_info = cursor.fetchall()
        password = (teacher_info[0])['password']
        if sha256_crypt.verify(password_candidate, password):
            title = request.form.get("title")
            body = request.form.get("body")
            conn.execute('''INSERT INTO collegeNotifications(title, body, teacher, date) VALUES(?, ?, ?, ?);''',
                         (title, body, teacher_id, current_time()))
            return "<h1>Success</h1>"

        else:
            return "<h1>Invalid Credentials !!</h1>"
    else:
        return "<h1>Add a notification using POST request.</h1>"


if __name__ == "__main__":
    app.run()
