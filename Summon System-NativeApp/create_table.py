import sqlite3

#define connection and cursor

connection = sqlite3.connect('databases.db')

cursor = connection.cursor()

#create store table

command1= '''CREATE TABLE "TicketTable" (
	"NoPlate"	TEXT,
	"IssueDate"	TEXT,
	"Location"	TEXT,
	"Offense"	TEXT,
	"Status"	TEXT,
	"Reportedby"	TEXT
)'''

cursor.execute(command1)