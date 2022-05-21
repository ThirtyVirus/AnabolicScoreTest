class Food:
    def __init__(self, name, weight, calories, fat, carbs, soluble_fiber, insoluble_fiber, protein):
        self.name = name
        self.weight = weight
        self.calories = calories
        self.fat = fat
        self.carbs = carbs
        self.soluble_fiber = soluble_fiber
        self.insoluble_file = insoluble_fiber
        self.protein = protein

    def get_calories_per_gram(self):
        return self.calories / self.weight

    def get_percent_weight_from_protein_fiber(self):
        weight_from_protein_fiber = self.protein + self.soluble_fiber + self.insoluble_file
        total_weight = self.fat + self.carbs + self.protein

        return (100 * weight_from_protein_fiber) / total_weight

    def get_percent_calories_from_fat(self):
        calories_from_fat = self.fat * 9
        calories_from_carbs = self.carbs * 4
        calories_from_carbs -= self.soluble_fiber * 2
        calories_from_carbs -= self.insoluble_file * 4
        calories_from_protein = self.protein * 4
        total_calories = calories_from_fat + calories_from_carbs + calories_from_protein

        return (100 * calories_from_fat) / total_calories
