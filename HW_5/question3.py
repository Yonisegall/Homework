def rosh_zanav(word):
    """
    This function received a word of type string and returns whether
    the word is "safe" or not. The criterion for a safe word is whether
    Naphthol always wins or not, no matter what Lehi chooses.

    :arg: word - string
    :return: True or False - if the word safe or not.
    """
    word_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9,
                 "j": 10,"k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17,
                 "r": 18, "s": 19,"t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
    result = True
    turn = True
    sum_l = 0
    sum_n = 0
    return rosh_zanav_wrap(word, word_dict, sum_l, sum_n, turn, result)


def rosh_zanav_wrap(word, word_dict, sum_l, sum_n, turn, result):
    """
    This function is a wrapper function to the main function.

    :arg: word - string
          word_dict - A dictionary that contains the geometry of all the letters
          sum_l - Leahy's points collection according to the letters he chose
          sum_n - Naftol's collection of points according to the letters he chose
          turn - A boolean variable that says whose turn it is to pick a letter
          result - A boolean variable that represents whether the word is safe or not

    :return: True or False - if the word safe or not
    """
    if len(word) == 0:
        if sum_l >= sum_n:
            result = False
        return result
    if not turn:
        if word_dict.get(word[0]) == word_dict.get(word[-1]):
            op_1 = rosh_zanav_wrap(word[1:], word_dict, sum_l, sum_n + word_dict.get(word[0]), not turn, result)
            op_2 = rosh_zanav_wrap(word[:-1], word_dict, sum_l, sum_n + word_dict.get(word[-1]), not turn, result)
            return op_1 and op_2
        if word_dict.get(word[0]) > word_dict.get(word[-1]):
            return rosh_zanav_wrap(word[1:], word_dict, sum_l, sum_n + word_dict.get(word[0]), not turn, result)
        else:
            return rosh_zanav_wrap(word[:-1], word_dict, sum_l, sum_n + word_dict.get(word[-1]), not turn, result)
    else:
        option_1 = rosh_zanav_wrap(word[1:], word_dict, sum_l + word_dict.get(word[0]), sum_n, not turn, result)
        option_2 = rosh_zanav_wrap(word[:-1], word_dict, sum_l + word_dict.get(word[-1]), sum_n, not turn, result)
        return option_1 and option_2

############################## Tests ########################################

##################### q.3 ##########################

print(rosh_zanav('asa') == True)
print(rosh_zanav('evyatar') == True)
print(rosh_zanav('breakfast') == False)
print(rosh_zanav('abcba') == False)
print(rosh_zanav('abcba') == False)
print(rosh_zanav('abccba') == False)
print(rosh_zanav('agfechij') == False)
print(rosh_zanav('aakaa') == False)
print(rosh_zanav("razba") == False)