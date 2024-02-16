############################# Q1 #############################
def verify_seating_arrangement(cinema):
    # Write your code here
    """
    Args:
        lists in one big list that all list
        it's row in cinema. There is seating
        restrictions in the cinema so the function
        checks if the order of the sitting according
        to the restrictions.
        1 - one man seating
        2 - one of couple.
        0 - no one seating.

    Returns:
           True or False - if the order of the
           sitting according to the restrictions.
    """
    seats = {}
    row = 0
    for r in cinema:
        column = 1
        row += 1
        l = 0
        while l < len(r):
            seat = (row,column)
            seats[seat] = r[l]
            column += 1
            l += 1
    result = True
    column = 1
    row = 1
    while row < len(cinema):
        while column < len(cinema[0]):
            seat = (row,column)
            if seats.get(seat) == 0:
                column += 1
                row += 1
            if seats.get(seat) == 1:
                if seats.get((row,column-1)) != 0 and seats.get((row,column-1)) != None:
                    return False
                if seats.get((row,column-2)) != 0 and seats.get((row,column-2)) != None:
                    return False
                if seats.get((row,column+1)) != 0 and seats.get((row,column+1)) != None:
                    return False
                if seats.get((row,column+2)) != 0 and seats.get((row,column+2)) != None:
                    return False
                if seats.get((row+1,column)) != 0 and seats.get((row+1,column)) != None:
                    return False
                if seats.get((row+2,column)) != 0 and seats.get((row+2,column)) != None:
                    return False
            if seats.get(seat) == 2:
                if seats.get((row,column-1)) == 2:
                    if seats.get((row,column-1)) != 2 and seats.get((row,column-1)) != None:
                        return False
                    if seats.get((row,column-2)) != 0 and seats.get((row,column-2)) != None:
                        return False
                    if seats.get((row,column+1)) != 0 and seats.get((row,column+1)) != None:
                        return False
                    if seats.get((row,column+2)) != 0 and seats.get((row,column+2)) != None:
                        return False
                    if seats.get((row+1,column)) != 0 and seats.get((row+1,column)) != None:
                        return False
                    if seats.get((row+2,column)) != 0 and seats.get((row+2,column)) != None:
                        return False
                else:
                    if seats.get((row,column-1)) != 0 and seats.get((row,column-1)) != None:
                        return False
                    if seats.get((row,column-2)) != 0 and seats.get((row,column-2)) != None:
                        return False
                    if seats.get((row,column+1)) != 2 and seats.get((row,column+1)) != None:
                        return False
                    if seats.get((row,column+2)) != 0 and seats.get((row,column+2)) != None:
                        return False
                    if seats.get((row+1,column)) != 0 and seats.get((row+1,column)) != None:
                        return False
                    if seats.get((row+2,column)) != 0 and seats.get((row+2,column)) != None:
                        return False
            column += 1
        row += 1
    return result
############################# Q2.1 #############################
def is_DNA (DNA_seq):
    # Write your code here
    """
    Args:
        string with DNA sequence.

    Returns:
        if the DNA sequence ok or not.
        if it's right - the function return the
        DNA sequence in list.
        if it's not right - the function return
        "Not DNA seq".
    """
    first_codon = "ATG"
    letters = "ATGC"
    stop_codon_1 = "TGA"
    stop_codon_2 = "TAG"
    stop_codon_3 = "TAA"
    new_DNA_seq = DNA_seq.split(" ")
    if len(new_DNA_seq) <= 1:
        return "Not DNA seq"
    if new_DNA_seq[0] != first_codon:
        return "Not DNA seq"
    if new_DNA_seq[-1] != stop_codon_1 and new_DNA_seq[-1] != stop_codon_2 and new_DNA_seq[-1] != stop_codon_3:
        return "Not DNA seq"
    for ind in range(len(new_DNA_seq)-1):
        code = new_DNA_seq[ind]
        for l in code:
            if l in letters:
                continue
            else:
                return "Not DNA seq"
        if len(code) != 3:
            return "Not DNA seq"
        if ind == 0 or ind == (len(new_DNA_seq) - 1):
            continue
        else:
            if code == stop_codon_1 or code == stop_codon_2 or code == stop_codon_3:
                return "Not DNA seq"
    return new_DNA_seq

############################ Q2.2 #############################
def DNA_to_RNA (DNA_seq):
    # Write your code here
    """
    Args:
        string with DNA sequence.

    Returns:
        RNA sequence in list.
        if the DNA sequence right - the function
        replace the letter "T" in "U".
        if the DNA sequence not right - the function return
        empty list [].
    """
    DNA_code = is_DNA(DNA_seq)
    if DNA_code == "Not DNA seq":
        return []
    else:
        new_RNA = []
        for i in DNA_code:
            i = i.replace("T","U")
            new_RNA.append(i)
        return new_RNA

############################# Q2.3 #############################
def codon_translator(codon):
    RNA_to_protien = {"UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
                      "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
                      "UAU": "Tyr", "UAC": "Tyr",
                      "UGU": "Cys", "UGC": "Cys", "UGG": "Trp",
                      "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
                      "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
                      "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
                      "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
                      "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
                      "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
                      "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
                      "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
                      "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
                      "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
                      "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
                      "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly", }
    decoding = RNA_to_protien.get(codon, "stop")
    return decoding

def RNA_to_Protein(DNA_seq):
    # Write your code here
    """
     Args:
         string with DNA sequence.

     Returns:
         if the DNA sequence right - the function return
         Amino acid sequence of the protein in tuple.
         if the DNA sequence not right - the function
         return empty tuple ().
     """
    new_RNA = DNA_to_RNA(DNA_seq)
    new_Protein = ()
    if new_RNA == []:
        return ()
    for i in new_RNA:
        if i == new_RNA[len(new_RNA)-1]:
            break
        RNA_1 = codon_translator(i)
        new_Protein = new_Protein + (RNA_1,)
    return new_Protein

############################# Q3.1 #############################
def ingredient_identifier(list_of_ingredients):
    # Write your code here
    """
     Args:
         A list of strins.
         The string made of - ingredient, nutritional value
         and boolean variable - if the ingredient vegan or not.

     Returns:
         Dictionary in dictionary that the key of
         the center dictionary is the ingredient, and
         the other dictionary made of the nutritional value
         and boolean variable - vegan or not.
    """
    products = {}
    for p in list_of_ingredients:
        values = {}
        lst_1 = p.split(":")
        lst_2 = lst_1[1].split(",")
        ingredient = lst_1[0]
        value = lst_2[0]
        value_nutritional = float(value)
        if lst_2[1][1] == "F":
            vegan = not bool(lst_2[1])
        else:
            vegan = bool(lst_2[1])
        values["nutritional_value"] = value_nutritional
        values["vegan"] = vegan
        products[ingredient] = values
    return products

############################# Q3.2 #############################
all_ingredients = ["Carrot: 123.4, True", "Sweet potato: 100.0, True", "Salmon: 120.0, False", "Cucumber: 90.0, True",
                       "Lettuce: 35.0, True", "Soya beans: 139.8, True", "Tofu: 260, True", "Red Meat: 400, False",
                       "Tuna: 360, False", "Tomato: 50, True", "Potato: 210, True", "Rice: 240, True",
                       "Green beans: 170.0, True", "Egg: 110.0, False", "Pasta: 266.6, True", "Mushrooms: 221.1, True",
                       "Green lentils: 220.9, True", "Pepper: 12.0, True", "Ricotta cheese: 233.4, False",
                       "Mozarella: 311.0, False", "Chicken: 220, False", "Salt: 0, True",
                       "Sugar: 141, True", "Unsalted butter: 321.0, False", "Olive: 120.0, True", "Bread: 140.0, True",
                       "Bell pepper: 119.8, True", "Onion: 121, True", "Broccoli: 12.1, True"]
def meal_calculator(recipe, all_ingredients_details):
    # Write your code here
    """
     Args:
         The function get two arguments:
         1. Recipe - dictionary that the keys is
         the type of the food in string and the value
         is the ingredients of the food in tuple.
         2. All ingredients details - dictionary with
         all the values from the previous function.

     Returns:
         Dictionary that the keys is the type of the food
         and the values is - the number of ingredients,
         the nutritional value and boolean variable - vegan
         or not in tuple.
    """
    meals = {}
    for i in recipe:
        meal_vegan = True
        meal_value = 0
        ingredients = recipe.get(i)
        num_ing = len(ingredients)
        for l in ingredients:
            products = all_ingredients_details.get(l)
            value = products.get('nutritional_value')
            vegan = products.get('vegan')
            meal_value += value
            if vegan == False:
                meal_vegan = False
        meals[i] = (num_ing, meal_value, meal_vegan)
    return meals

############################# Q3.3 #############################
def popular_meal(meals_info):
    # Write your code here
    """
     Args:
         Dictionary that the keys is the type
         of the food and the values is the number
         of reservations of this food in the restaurant .

     Returns:
         Tuple with the type of the food
         with the most reservations and the
         frequency of it's reservations
    """
    most_orders = 0
    most_meal = ""
    num_of_orders = 0
    for i in meals_info:
        value = meals_info.get(i)
        num_of_orders += value
        if value > most_orders:
            most_orders = value
            most_meal = i
    frequency = most_orders/num_of_orders
    most_meal_1 = most_meal.upper()
    return (most_meal_1, frequency)


########################### Tests ############################

############################# Q1 #############################
# tests for function - verify_seating_arrangement:
cinima_1 = [
           [0,0,2,2,0,0,1],
           [1,0,0,0,1,0,0],
           [0,1,0,0,0,1,0]]
cinima_2 = [
           [1,0,0,1,0,0,1],
           [0,0,1,0,0,1,0],
           [0,1,0,0,1,0,0]]
cinima_3 = [
           [1,0,0,1,0,0,1],
           [0,0,0,2,2,1,0],
           [0,1,0,0,1,0,0]]
cinima_4 = [
           [2,0,0,1,0,0,1],
           [0,0,1,0,0,1,0],
           [0,1,0,0,1,0,0]]

cinima_5 = [[1]]
cinima_6 = [
           [2,0,0],
           [0,0,0]]
# print(verify_seating_arrangement(cinima_1))

############################# Q2.1 #############################
# tests for function - is_DNA:
sec_1 = "ATG ATT TTA GCA CGA TGC TGC TTA TAA"
sec_2 = "AGG ATT TTA GCA CCC GCA GCC CCC TGA"
sec_3 = "ATG AGG AGC CGA CCC GCA GCC CCC TGA"
sec_4 = "ATG AGG AGC TGA CCC GCA GCC CCC TGA"
sec_5 = "ATG AGG AGC TGA CCC GCA GCC CCC TTT"
sec_6 = "I love Python"
sec_7 = "ATG TAA"
sec_8 = ""
# print(is_DNA(sec_1))

############################# Q2.2 #############################
# tests for function - DNA_to_RNA:
sample_1 = "ATG CGG AAA GGG CCC GCA GCC CCC GGC CCG AAT TTT AAA TAT TGA"
sample_2 = "CGG TTT CCG CGC GCT GTC CTC TGC CTG TAT TTT ATA TCT CGA TAA"
sample_3 = ""
# print(DNA_to_RNA(sample_1))

############################# Q2.3 #############################
# tests for function - RNA_to_Protein:
sampl_1 = "ATG CGG AAA GGG CCC GCA GCC CCC GGC CCG AAT TTT AAA TAT TGA"
sampl_2 = "CGG TTT CCG CGC GCT GTC CTC TGC CTG TAT TTT ATA TCT CGA TAA"
sampl_3 = " "
# print(RNA_to_Protein(sampl_3))

############################# Q3.1 #############################
# tests for function - ingredient_identifier:
i = ["Salmon: 150.7, False", "Carrot: 30.5, True"]
y = []
# print(ingredient_identifier()

############################# Q3.2 #############################
# tests for function - meal_calculator:
recipe = {"Chicken Salad": ("Sugar", "Carrot", "Chicken", "Onion"),
          "Tofu with vagetables": ("Tofu", "Sugar", "Rice", "Onion", "Broccoli", "Potato", "Carrot")}
all_ingredients_details = ingredient_identifier(all_ingredients)
# print(meal_calculator(recipe, all_ingredients_details))

############################# Q3.3 #############################
# tests for function - popular_meal:
meals_info = {"Chicken salad": 13, "Chicken": 21, "Red meat": 2, "Rice with chicken and vagetables": 34}
# print(popular_meal(meals_info))















