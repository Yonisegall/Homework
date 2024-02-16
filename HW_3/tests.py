import assignment3 as a3


def check_verify_seating_arrangement():
    cinema = [
        [0, 0, 2, 2, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0]
    ]
    if not a3.verify_seating_arrangement(cinema):
        return False
    cinema = [
        [1, 0, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 0]
    ]
    if not a3.verify_seating_arrangement(cinema):
        return False
    cinema = [
        [1, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 2, 2, 1, 0],
        [0, 1, 0, 0, 1, 0, 0]
    ]
    if a3.verify_seating_arrangement(cinema):
        return False
    cinema = [
        [2, 0, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 0]
    ]
    if a3.verify_seating_arrangement(cinema):
        return False
    return True


def check_is_DNA():
    seq1 = "ATG ATT TTA GCA CGA TGC TGC TTA TAA"
    DNA1 = seq1.split(" ")
    if not a3.is_DNA(seq1) == DNA1:
        return False
    seq2 = "AGG ATT TTA GCA CGA TGC TGC TTA TAA"
    if not a3.is_DNA(seq2) == "Not DNA seq":
        return False
    seq3 = "ATG AGG AGC CGA CCC GCA GCC CCC TGA"
    DNA3 = seq3.split(" ")
    if not a3.is_DNA(seq3) == DNA3:
        return False
    seq4 = "ATG AGG AGC TGA CCC GCA GCC CCC TGA"
    if not a3.is_DNA(seq4) == "Not DNA seq":
        return False
    seq5 = "ATG AGG AGC TGA CCC GCA GCC CCC TTT"
    if not a3.is_DNA(seq5) == "Not DNA seq":
        return False
    seq6 = "I love Python"
    if not a3.is_DNA(seq6) == "Not DNA seq":
        return False
    return True


def check_DNA_to_RNA():
    seq1 = "ATG CGG AAA GGG CCC GCA GCC CCC GCC CCG AAT TTT AAA TAT TGA"
    RNA1 = seq1.replace("T", "U").split(" ")
    if not a3.DNA_to_RNA(seq1) == RNA1:
        return False
    seq2 = "CGG TTT CCG CGC GCT GTC CTC TGC CTG TAT TTT ATA TCT CGA TAA"
    if not a3.DNA_to_RNA(seq2) == []:
        return False
    return True


def check_RNA_to_Protein():
    seq1 = "ATG CGG AAA GGG CCC GCA GCC CCC GGC CCG AAT TTT AAA TAT TGA"
    tup = ('Met', 'Arg', 'Lys', 'Gly', 'Pro', 'Ala', 'Ala', 'Pro', 'Gly', 'Pro', 'Asn', 'Phe', 'Lys', 'Tyr')
    if not a3.RNA_to_Protein(seq1) == tup:
        return False
    seq2 = "CGG TTT CCG CGC GCT GTC CTC TGC CTG TAT TTT ATA TCT CGA TAA"
    if not a3.RNA_to_Protein(seq2) == ():
        return False
    return True


def check_ingredient_identifier():
    input_ingredients = ["Salmon: 150.7, False", "Carrot: 30.5, True"]
    output = a3.ingredient_identifier(input_ingredients)
    if not output == {'Salmon': {'nutritional_value': 150.7, 'vegan': False},
                      'Carrot': {'nutritional_value': 30.5, 'vegan': True}}:
        return False
    return True


def check_meal_calculator():
    all_ingredients = ["Carrot: 123.4, True", "Sweet potato: 100.0, True", "Salmon: 120.0, False",
                       "Cucumber: 90.0, True",
                       "Lettuce: 35.0, True", "Soya beans: 139.8, True", "Tofu: 260, True", "Red Meat: 400, False",
                       "Tuna: 360, False", "Tomato: 50, True", "Potato: 210, True", "Rice: 240, True",
                       "Green beans: 170.0, True", "Egg: 110.0, False", "Pasta: 266.6, True", "Mushrooms: 221.1, True",
                       "Green lentils: 220.9, True", "Pepper: 12.0, True", "Ricotta cheese: 233.4, False",
                       "Mozarella: 311.0, False", "Chicken: 220, False", "Salt: 0, True",
                       "Sugar: 141, True", "Unsalted butter: 321.0, False", "Olive: 120.0, True", "Bread: 140.0, True",
                       "Bell pepper: 119.8, True", "Onion: 121, True", "Broccoli: 12.1, True"]

    recipes = {"Chicken Salad": ("Sugar", "Carrot", "Chicken", "Onion"),
               "Tofu with vegetables": ("Tofu", "Sugar", "Rice", "Onion", "Broccoli", "Potato", "Carrot")}
    all_ingredients_details = a3.ingredient_identifier(all_ingredients)
    output = a3.meal_calculator(recipes, all_ingredients_details)
    if not output == {"Chicken Salad": (4, 605.4, False), "Tofu with vegetables": (7, 1107.5, True)}:
        return False
    return True


def check_popular_meal():
    requested_meal = {"Chicken Salad": 13, "Chicken": 21, "Red meat": 2, "Rice with vegetables": 34}
    output = a3.popular_meal(requested_meal)
    if not output == ('RICE WITH VEGETABLES', 0.4857142857142857):
        return False
    return True


def main():
    if check_verify_seating_arrangement():
        print("q1 is working")
    else:
        print("q1 has a problem")
    if check_is_DNA():
        print("q2.1 is working")
    else:
        print("q2.1 has a problem")
    if check_DNA_to_RNA():
        print("q2.2 is working")
    else:
        print("q2.2 has a problem")
    if check_RNA_to_Protein():
        print("q2.3 is working")
    else:
        print("q2.3 has a problem")
    if check_ingredient_identifier():
        print("q3.1 is working")
    else:
        print("q3.1 has a problem")
    if check_meal_calculator():
        print("q3.2 is working")
    else:
        print("q3.2 has a problem")
    if check_popular_meal():
        print("q3.3 is working")
    else:
        print("q3.3 has a problem")


if __name__ == '__main__':
    main()
