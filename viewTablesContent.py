import sqlite3


def dict_factory(cursor_, row_):
    d = {}
    for idx, col in enumerate(cursor_.description):
        d[col[0]] = row_[idx]
    return d


conn = sqlite3.connect('kmvOnline.db')
conn.row_factory = dict_factory
cursor = conn.cursor()

print("collegeNotifications :: ")
cursor.execute("SELECT * from collegeNotifications;")
for row in cursor.fetchall():
    print(row)

print("teachersInfo :: ")
cursor.execute("SELECT * from teachersInfo;")
for row in cursor.fetchall():
    print(row)
