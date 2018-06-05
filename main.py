import sqlite3
import pandas as pd

try:
    conn = sqlite3.connect('food.db')
except sqlite3.OperationalError:
    print("Could not connect to food.db.")

c = conn.cursor()

try:
    c.execute('''CREATE TABLE foods(food TEXT, calories INTEGER, protein INTEGER)''')
    conn.commit()
    print("Foods table didn't exist so we created.")
except sqlite3.OperationalError:
    print("Foods table is present.")

try:
    c.execute('''CREATE TABLE diary(dateID INTEGER, food TEXT, weight INTEGER)''')
    conn.commit()
    print("Diary table didn't exist so we created.")
except sqlite3.OperationalError:
    print("Diary table is present.")

dates = pd.date_range(start='2018-01-01', end='2018-01-31')
date_dateID_dict = {}
i = 0
for date in dates.astype(str):
    i = i + 1
    date_dateID_dict[date] = i

chosen = ""

def get_choice():
    choice = ""
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "exit":
        choice = input("""
        [1]: Add item to food table.
        [2]: Add food serving to diary table.
        [3]: Print food table.
        [4]: Print diary table.
        [5]: Group diary entries and summarise.
        [6]: Edit food nutrient values.
        [exit]: Exit program.
        """)
    return choice

while chosen != "exit":

    chosen = get_choice()

    if chosen == "1":
        food, protein, calories = input("Enter: food, protein/100g, calories/100g\n").split(", ")
        c.execute("INSERT INTO food VALUES(?, ?, ?)", (food, calories, protein))
    if chosen == "2":
        dateID, food, weight = input("Enter: dateID, food, weight\n").split(", ")
        c.execute("INSERT INTO diary VALUES(?, ?, ?)", (dateID, food, weight))
    if chosen == "3":
        c.execute("SELECT name, calories, protein FROM foods ")
        print(c.fetchall())
    if chosen == "4":
        c.execute("SELECT dateID, food, weight FROM diary")
        print(c.fetchall())
    if chosen == "5":
        c.execute("SELECT foodname FROM diary")
        print(c.fetchall())
    if chosen == "6":
        food, protein, calories = input("Enter: food, protein/100g, calories/100g\n").split(", ")
        c.execute("UPDATE foods SET calories = ?, protein = ? WHERE name = ?", (calories, protein, food))
    if chosen == "7":
        #c.execute("SELECT dateID, date, calories, protein FROM summary")
        #print(c.fetchall())
        c.execute("DROP TABLE diary")
        #c.execute("ALTER TABLE food RENAME TO foods")

    conn.commit()

conn.close()


#try:
#    c.execute('''CREATE TABLE summary(dateID INTEGER PRIMARY KEY, date DATE, calories INTEGER, protein INTEGER)''')
#    dates = pd.date_range(start='2018-01-01', end='2018-01-31')
#    for date in dates.astype(str):
#        c.execute("INSERT INTO summary VALUES(NULL, ? , NULL, NULL)", (date,))
#    conn.commit()
#    print("Summary table didn't exist so we created.")
#except sqlite3.OperationalError:
#    print("Summary table is present.")