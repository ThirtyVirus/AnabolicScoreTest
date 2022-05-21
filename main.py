# coding=utf-8

from food import Food

egg_whites = Food("Egg Whites", 46.0, 25.0, 0.0, 0.0, 0.0, 0.0, 5.0)
unsweetened_almond_milk = Food("Unsweetened Almond Milk", 260.0, 30.0, 2.5, 1.0, 0.0, 0.0, 1.0)
chicken_breast = Food("Chicken Breast", 112.0, 120.0, 1.5, 0.0, 0.0, 0.0, 26.0)
keto_white_bread = Food("Keto White Bread", 28.0, 35.0, 1.0, 10.0, 0.0, 10.0, 4.0)
greek_yogurt_bar = Food("Yasso Greek Yogurt Bar", 65.0, 100.0, 2.0, 16.0, 0.0, 0.0, 5.0)
elevation_base20_bar = Food("Elevation Base 20 Protein Bar", 60.0, 220.0, 9.0, 23.0, 7.0, 0.0, 20.0)
double_stuffed_oreo = Food("Double Stuffed Oreo", 29.0, 140.0, 7.0, 21.0, 0.0, 0.0, 0.0)
doritos_nacho_cheese = Food("Doritos Nacho Cheese", 28.0, 150.0, 8.0, 18.0, 1.0, 0.0, 2.0)


def get_scores(food):
    calories_per_gram = food.get_calories_per_gram()
    percent_weight_from_protein_fiber = food.get_percent_weight_from_protein_fiber()
    percent_calories_from_fat = food.get_percent_calories_from_fat()

    # assuming a maximum of 9 calories per gram of a food (pure fat)
    volume_score = (((9 - food.get_calories_per_gram()) * 10) / 9) * 7.5

    thermic_score = percent_weight_from_protein_fiber / 8.0
    lean_score = (100 - percent_calories_from_fat) / 8.0

    print "-----------------------------------------"
    print food.name
    print "  ", round(calories_per_gram, 2), "Calories Per Gram"
    print "  ", round(percent_weight_from_protein_fiber, 2), "% Protein and Fiber by Weight"
    print "  ", round(percent_calories_from_fat, 2), "% Calories from Fat"
    print ""
    print "  ", round(volume_score, 2), "/ 75 Volume Score"
    print "  ", round(thermic_score, 2), "/ 12.5 Thermic Score"
    print "  ", round(lean_score, 2), "/ 12.5 Lean Score"
    print ""
    print "  ", round(volume_score + thermic_score + lean_score, 2), "Total Anabolic Score"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_scores(egg_whites)
    get_scores(chicken_breast)
    get_scores(unsweetened_almond_milk)
    get_scores(keto_white_bread)
    get_scores(greek_yogurt_bar)
    get_scores(elevation_base20_bar)
    get_scores(double_stuffed_oreo)
    get_scores(doritos_nacho_cheese)
