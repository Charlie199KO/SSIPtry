import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

insert = f"INSERT INTO Form VALUES()"