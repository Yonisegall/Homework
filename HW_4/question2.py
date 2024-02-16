def string_overlap_detector(core, rep, repetition):
    """
    :param: core - the core string
    :param: rep - the repeat string
    :param: repetition - A non-negative integer. It's a guess
            how many times rep exist in core


    :return: True or False if the repetition equal to the numbers
             of time that rep in core.
    """
    ##Code ##
    return str_over_det_2(core, rep, repetition, 0)

def str_over_det_2(core, rep, repetition, count):
    """
    :param: core - The core string
    :param: rep - The repeat string
    :param: repetition - A non-negative integer. It's a guess
            how many times rep exist in core.
    :param: len_rep - length of core string.
    :param: count - counter for times that rep exist in core.


    :return: True or False if count even to the repetition.

    """
    ##Code ##
    if len(core) == 0:
        if count == repetition:
            return True
        else:
            return False
    if core[:len(rep)] == rep:
        count += 1
        return str_over_det_2(core[1:], rep, repetition, count)
    else:
        return str_over_det_2(core[1:], rep, repetition, count)


def string_overlap_dual(string_1, string_2, repetition):
    """
    :param: string_1 - A string
    :param: string_2 - A string
    :param: repetition - A non-negative integer. It's a guess
            how many times string_1 and string_2 exist in each other.

    :return: True or False if the repetition equal to the numbers
             of time that string_1 and string_2 in each others.
    """
    ##Code ##
    option_1 = string_overlap_detector(string_1, string_2, repetition)
    option_2 = string_overlap_detector(string_2, string_1, repetition)
    if option_1 == False and option_2 == False:
        return False
    else:
        return True

################################-Tests-#####################################

########################## Q.2.1 #################################

# print(string_overlap_detector('saba sababa', 'aba', 2) == False)
# print(string_overlap_detector('saba sababa', 'aba', 3) == True)
# print(string_overlap_detector("", 'a', 0)  == True)
# print(string_overlap_detector("ab",'ab',0)  == False)
# print(string_overlap_detector("ab",'ab',1)  == True)
# print(string_overlap_detector("abbgbgabglidjfabfkjdikfababab",'ab',6)  == True)
# print(string_overlap_detector("i was a navy seals officer",'a',4)  == True)
# print(string_overlap_detector("i was a navy seals officer",'a',3)  == False)
# print(string_overlap_detector("i was a navy seals officer",'a',5)  == False)
# print(string_overlap_detector("i was a navy seals officer",'navy',0) == False)
# print(string_overlap_detector("hey kid", "clown",0)  == True)

########################## Q.2.2 #################################

# print(string_overlap_dual("saba sababa", "aba", 2) == False)
# print(string_overlap_dual("saba sababa", "aba", 3) == True)
# print(string_overlap_dual("", "ab", 0)  == True)
# print(string_overlap_dual("ab","ab",0)  == False)
# print(string_overlap_dual("ab","ab",1)  == True)
# print(string_overlap_dual("abbgbgabglidjfabfkjdikfababab",'ab',6)  == True)
# print(string_overlap_dual("i was a navy seals officer",'a',4)  == True)
# print(string_overlap_dual("i was a navy seals officer",'a',3)  == False)
# print(string_overlap_dual("i was a navy seals officer",'a',5)  == False)
# print(string_overlap_dual("i was a navy seals officer",'navy',0) == True)
# print(string_overlap_dual("hey kid", "clown",0)  == True)
# print(string_overlap_dual("wa","which witch watch which watch", 2)  == True)
# print(string_overlap_dual("which witch watch which watch", "wa", 2)  == True)
# print(string_overlap_dual("which witch watch which watch", "ch", 4)  == False)
# print(string_overlap_dual("aaaaaa", "aa", 5) == True)
