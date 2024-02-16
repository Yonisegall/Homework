def count_coin_sets(money_value, list_of_coins):
    """
    The function received a non-negative number and a list of coins values. The function
    calculates how many possible ways there are to represent the number by the coins.

    :arg: money_value - A non-negative integer
          list_of_coins - A list with coins value

    :return: The number of ways the number can be represented by the types of coins
    """
    sort_lst = sorted(list_of_coins, reverse=True)
    dict_1 = {}
    count = 0
    if money_value == 0:
        return 0
    return count_coin_sets_wrap(money_value, sort_lst, dict_1, count)


def count_coin_sets_wrap(money_value, sort_lst, dict_1, count):
    """
    This function is a wrapper function to the main function.

    :arg: money_value - A non-negative integer
          sort_list - A sorted list with coins value
          dict_1 - An empty dictionary that stores the values in it
          count -A variable that stores the number of times the number
                 can be represented by the types of coins

    :return: The number of ways the number can be represented by the types of coins
    """
    if count == money_value:
        return 1
    if count > money_value:
        return 0
    if len(sort_lst) == 0:
        return 0
    in_dict = dict_1.get((count, tuple(sort_lst)), False)
    if not in_dict:
        option_1 = count_coin_sets_wrap(money_value, sort_lst, dict_1, count + sort_lst[0])
        option_2 = count_coin_sets_wrap(money_value, sort_lst[1:], dict_1, count)
        dict_1[(count, tuple(sort_lst))] = option_1 + option_2
    return dict_1[(count, tuple(sort_lst))]


##################### without memo ###########################
    # option_1 = count_coin_sets_2(money_value, sort_lst, dict_1, count + sort_lst[0])
    # option_2 = count_coin_sets_2(money_value, sort_lst[1:], dict_1, count)
    # return option_1 + option_2
############################## Tests ########################################

##################### q.2 ##########################
print(count_coin_sets(2, [10, 5, 2, 1]) == 2)
print(count_coin_sets(6, [2, 10, 5, 1]) == 5)
print(count_coin_sets(12, [1, 2, 10, 5]) == 15)
print(count_coin_sets(0, [10, 5, 2, 1]) == 0)
print(count_coin_sets(10, [10, 5, 2, 1]) == 11)
print(count_coin_sets(3, [3, 5, 2, 1]) == 3)
print(count_coin_sets(2, [3, 5, 7, 4]) == 0)

########### Max ##############

# print(count_coin_sets(2978, [3, 5, 7, 4]))
print(count_coin_sets(9883, [1, 2, 5, 10]) == 1613246910)

