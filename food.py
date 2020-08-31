# research sparksee for storing objects

class Food:

"""
The Food class allows Food objects to be created which define
the calories, protein, carbs and fat per 100g of the named food.

"""

    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat


class Meal:

#Foodxquantity        

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