import sqlite3

db_connection = sqlite3.connect("sqlite.db")
print(db_connection)

db_cursor = db_connection.cursor()
print(db_cursor)

query1 = "SELECT * FROM demo"
db_cursor.execute(query1)
print("reading one row")
row = db_cursor.fetchone()
print(row)

print("reading two row")
rows = db_cursor.fetchmany(2)
print(rows)

print("reading all rows")
rows = db_cursor.fetchall()
for r in rows:
    print(r)

query2 = "INSERT INTO demo (Name, Hint) VALUES ('Micheal','Murphy')"
db_cursor.execute(query2)
db_connection.commit()

query3 = "SELECT * FROM demo WHERE ID > 20"
#db_cursor.execute(query3)
#function.query_result = (db_cursor,"fetchall")
