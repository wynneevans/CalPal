# research sparksee for storing objects

class Food:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        

class FoodList:
    def __init__(self):
        self.foods = {}

    def add_food(self, food, weight):
        self.foods[food] = weight

    def delete_food(self, food):
        del self.foods[food]

    def total(self, nutrient, food_dict):
        total = 0
        for food in self.foods:
            total += food_dict[food].nutrition[nutrient]*self.foods[food]/100
        return total