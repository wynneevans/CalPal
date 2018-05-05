from food import *
import pickle

food_dict = {}
calendar = {}

try:
    food_dict = pickle.load(open("foods.dat", "rb"))
except Exception:
    print("Could not open food dictionary")

try:
    calendar = pickle.load(open("calendar.dat", "rb"))
except Exception:
    print("Could not open food calendar")

choice = None

print("""
[1]: Add food to global list.
[2]: Add food to date list.
[3]: Print foods in global list.
[4]: Print calorie intake for each calendar entry.
[5]: Print protein intake for each calendar entry.
[exit]: Exit program.
""")

while choice != "exit":

    choice = input()

    if choice == "1":
        food, protein, calories = input("Enter: food, protein/100g, calories/100g\n").split(" ")
        food_dict[food] = Nutrients(int(protein), int(calories))
    if choice == "2":
        date, food_1, weight_1, food_2, weight_2 = input("Enter: date, food 1, weight 1, food 2, weight 2\n").split(" ")
        calendar[date] = FoodList()
        calendar[date].add_food(food_1, int(weight_1))
        calendar[date].add_food(food_2, int(weight_2))
    if choice == "3":
        for food in food_dict:
            print(food, food_dict[food].nutrition)
    if choice == "4":
        print("Calorie (kcal) Intake:")
        for date in calendar:
            print("{}: {}".format(date, calendar[date].total("calories", food_dict)))
    if choice == "5":
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
