import sqlite3

db_file = 'database.db'

db = None
db = sqlite3.connect(db_file)
c = db.cursor()

#Stats
c.execute("CREATE TABLE if not Exists stats(strength INTERGER, fortitude INTEGER, agility INTEGER, intelligence INTEGER, willpower INTEGER, charisma INTEGER)")
#Personal
c.execute("CREATE TABLE if not Exists person(name TEXT, age INTEGER, level INTEGER)")

