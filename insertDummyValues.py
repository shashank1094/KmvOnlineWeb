import sqlite3
from datetime import datetime
from passlib.hash import sha256_crypt


def current_time():
    return str(datetime.now())


conn = sqlite3.connect('kmvOnline.db')
cursor = conn.cursor()

dummyValues = [("First Notification", "This is the body of first notification.", 1, current_time()),
               ("Second Notification", "This is the body of second notification.", 2, current_time()),
               ("Third Notification", "This is the body of third notification.", 3, current_time())]

cursor.executemany("INSERT INTO collegeNotifications(title, body, teacher, date) VALUES(?, ?, ?, ?);", dummyValues)

dummyValues = [("teacher1", "Teacher One", sha256_crypt.encrypt("teacher1")),
               ("teacher2", "Teacher Two", sha256_crypt.encrypt("teacher2")),
               ("teacher3", "Teacher Three", sha256_crypt.encrypt("teacher3"))]

cursor.executemany("INSERT INTO teachersInfo(username, name, password) VALUES(?, ?, ?);", dummyValues)

conn.commit()
