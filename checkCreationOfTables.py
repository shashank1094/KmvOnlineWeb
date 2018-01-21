import sqlite3

conn = sqlite3.connect('kmvOnline.db')
cursor = conn.cursor()

cursor.execute('''PRAGMA table_info(sqlite_master);''')
columns = []
for columnInfo in cursor.fetchall():
    columns.append(columnInfo[1])
print("Columns in sqlite_master table ::", columns)

cursor.execute('''select name from sqlite_master where type = "table";''')
tables = []
for tableName in cursor.fetchall():
    tables.append(tableName[0])

print("All tables in DataBase ::", tables)
