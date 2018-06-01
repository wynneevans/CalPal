from food import *
import pickle

food_dict = {}
calendar = {}

try:
    food_dict = pickle.load(open("foods.dat", "rb"))
except Exception:
    print("Could not open food database.")

try:
    calendar = pickle.load(open("calendar.dat", "rb"))
except Exception:
    print("Could not open food calendar")

chosen = ""

def get_choice():
    choice = ""
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "exit":
        choice = input("""
        [1]: Add food to global list.
        [2]: Add food to date list.
        [3]: Print foods in global list.
        [4]: Print calorie intake for each calendar entry.
        [5]: Print protein intake for each calendar entry.
        [exit]: Exit program.
        """)
    return choice

while chosen != "exit":

    chosen = get_choice()

    if chosen == "1":
        food, protein, calories = input("Enter: food, protein/100g, calories/100g\n").split(" ")
        food_dict[food] = Nutrients(int(protein), int(calories))
    if chosen == "2":
        date, food_1, weight_1, food_2, weight_2 = input("Enter: date, food 1, weight 1, food 2, weight 2\n").split(" ")
        calendar[date] = FoodList()
        calendar[date].add_food(food_1, int(weight_1))
        calendar[date].add_food(food_2, int(weight_2))
    if chosen == "3":
        for food in food_dict:
            print(food, food_dict[food].nutrition)
    if chosen == "4":
        print("Calorie (kcal) Intake:")
        for date in calendar:
            print("{}: {}".format(date, calendar[date].total("calories", food_dict)))
    if chosen == "5":
        print("Protein (g) Intake:")
        for date in calendar:
            print("{}: {}".format(date, calendar[date].total("protein", food_dict)))


try:
    pickle.dump(food_dict, open("foods.dat", "wb"))
except Exception:
    print("Could not save food dictionary")

try:
    pickle.dump(calendar, open("calendar.dat", "wb"))
except Exception:
    print("Could not save calendar")
