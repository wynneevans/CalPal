class Nutrients:
    def __init__(self, protein, calories):
        self.protein = protein
        self.calories = calories
        self.nutrition = {"protein": self.protein, "calories": self.calories}

    def edit_protein(self, protein_update):
        self.nutrition = {"protein": protein_update, "calories": self.calories}

    def edit_calories(self, calories_update):
        self.calories = {"protein": self.protein, "calories": calories_update}


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