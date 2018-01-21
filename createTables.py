import sqlite3

conn = sqlite3.connect('kmvOnline.db')
cursor = conn.cursor()

cursor.execute('''drop table if exists collegeNotifications''')

cursor.execute('''CREATE TABLE collegeNotifications
(notificationid INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(100) NOT NULL,
body VARCHAR(500) NOT NULL,
teacher INTEGER NOT NULL,
date TEXT NOT NULL);''')

cursor.execute('''drop table if exists teachersInfo''')

cursor.execute('''CREATE TABLE teachersInfo
(teacherid INTEGER PRIMARY KEY AUTOINCREMENT,
username VARCHAR(100) NOT NULL,
name VARCHAR(500) NOT NULL,
password VARCHAR(1000) NOT NULL);''')

conn.commit()
