import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

try:
    conn = sqlite3.connect('food.db')
except sqlite3.OperationalError:
    print("Could not connect to food.db.")

c = conn.cursor()

try:
    c.execute('''CREATE TABLE foods(food TEXT, calories REAL , 
                    protein REAL, carbohydrate REAL, sugar REAL, fat REAL, 'saturated fat' REAL)''')
    conn.commit()
    print("Foods table didn't exist so it was created.")
except sqlite3.OperationalError:
    print("Foods table is present.")

try:
    c.execute('''CREATE TABLE diary(date DATE, food TEXT, weight REAL)''')
    conn.commit()
    print("Diary table didn't exist so it was created.")
except sqlite3.OperationalError:
    print("Diary table is present.")

dates = pd.date_range(start='2018-01-01', end='2020-01-01')
date_dateID_dict = {}
i = 0
for date in dates.astype(str):
    i = i + 1
    date_dateID_dict[i] = date

chosen = ""
summary = []

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
        food, calories, protein, carbohydrate, sugar, fat, sat_fat = input('''Enter food name and nutrient information per 100g: 
        food, calories, protein, carbohydrate, sugar, fat, saturated fat\n''').split(", ")
        c.execute("INSERT INTO foods VALUES(?, ?, ?, ?, ?, ?, ?)", (food, calories, protein, carbohydrate, sugar, fat, sat_fat))
    if chosen == "2":
        date, food, weight = input("Enter: date, food, weight\n").split(", ")
        c.execute("INSERT INTO diary VALUES(?, ?, ?)", (date, food, weight))
    if chosen == "3":
        c.execute("SELECT food, calories, protein, carbohydrate, sugar, fat, `saturated fat` FROM foods ")
        print(c.fetchall())
    if chosen == "4":
        c.execute("SELECT date, food, weight FROM diary")
        print(c.fetchall())
    if chosen == "5":
        c.execute('''SELECT diary.date, SUM(diary.weight * foods.calories) / 100, SUM(diary.weight * foods.protein) / 100, 
        SUM(diary.weight * foods.carbohydrate) / 100, SUM(diary.weight * foods.sugar) / 100, 
        SUM(diary.weight * foods.fat) / 100, SUM(diary.weight * foods.`saturated fat`) / 100
        FROM diary LEFT JOIN foods ON foods.food = diary.food 
        GROUP BY diary.date''')
        summary = c.fetchall()
        print(len(summary))
        x = [i for i in range(1,len(summary)+1)]
        print(x)
        plt.bar([i[0] for i in summary], [i[1] for i in summary])
        plt.title("Calories Consumed per Day")
        plt.ylabel("kcal")
        plt.show()

        plt.bar([i-0.3 for i in x], [i[2] for i in summary], width=0.15, label="Protein")
        plt.bar([i-0.15 for i in x], [i[3] for i in summary], width=0.15, label="Carbohydrate")
        plt.bar(x, [i[4] for i in summary], width=0.15, label="Sugar")
        plt.bar([i+0.15 for i in x], [i[5] for i in summary], width=0.15, label="Fat")
        plt.bar([i+0.3 for i in x], [i[6] for i in summary], width=0.15, label="Saturated Fat")
        plt.xticks(x, [date_dateID_dict[i] for i in x])
        plt.title("Macronutrients Consumed per Day")
        plt.ylabel("grams")
        plt.legend()#, "Carbohydrate", "Sugar", "Fat", "Saturated Fat")
        plt.show()
    if chosen == "6":
        table, column2, row, column1, value = input("Enter: table, search_column, search_col_entry, update_col_name, update_col_entry\n").split(", ")
        print(table, row, column1, column2, value)
        command = "UPDATE " + table + " SET " + column1 +  " = ? WHERE " + column2 + " = ?"
        c.execute(command, (value, row))
    #if chosen == "7":
    #    a = conn.execute('select * from foods')
        #names = list(map(lambda x: x[0], a.description))
        #print(names)
        #print(date_dateID_dict)
        #c.execute("SELECT dateID, date, calories, protein FROM summary")
        #print(c.fetchall())
        #c.execute("DROP TABLE diary")
        #c.execute("DROP TABLE foods")
        #c.execute("ALTER TABLE food RENAME TO foods")


    conn.commit()

conn.close()

