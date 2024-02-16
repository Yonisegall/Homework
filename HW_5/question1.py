def matrix_explorer(n, m):
    """
    This function received two non-negative integers that the numbers
    represent the number of the columns and the rows of a table and return
    the number of the shorted ways to get from one corner of the table to the other.

    :arg: n - non-negative number (the number of the columns of the table)
          m - non-negative number (the number of the rows of the table)

    :return: The number of the shortest paths that exist to get from one end of
             the rectangle to its other end.
    """
    if n == 1 or m == 1:
        return 1
    option_1 = matrix_explorer(n - 1, m)
    option_2 = matrix_explorer(n, m - 1)
    return option_1 + option_2


def matrix_explorer_memo(n, m):
    """
    This function received two non-negative integers that the numbers
    represent the number of the columns and the rows of a table and return
    the number of the shorted ways to get from one corner of the table to the other.

    :arg: n - non-negative number (the number of the columns of the table)
          m - non-negative number (the number of the rows of the table)

    :return: The number of the shortest paths that exist to get from one end of
             the rectangle to its other end.
    """
    dict_1 = {}
    return matrix_explorer_memo_wrap(n, m, dict_1)


def matrix_explorer_memo_wrap(n, m, dict_1):
    """
    This function is a wrapper function to the main function.

    :arg: n - non-negative number (the number of the columns of the table)
          m - non-negative number (the number of the rows of the table)
          dict_1 - An empty dictionary that stores the values in it.

    :return: The number of the shortest paths that exist to get from one end of
             the rectangle to its other end.
    """
    if n == 1 or m == 1:
        return 1
    in_dict = dict_1.get((n, m), False)
    if not in_dict:
        option_1 = matrix_explorer_memo_wrap(n - 1, m, dict_1)
        option_2 = matrix_explorer_memo_wrap(n, m - 1, dict_1)
        dict_1[(n, m)] = option_1 + option_2
    return dict_1[(n, m)]


###################### Tests ########################################

##################### q.1.1 ##########################
print(matrix_explorer(3, 2) == 3)
print(matrix_explorer(12, 9) == 75582)
print(matrix_explorer(1, 1) == 1)
print(matrix_explorer(2, 2) == 2)
print(matrix_explorer(1, 2) == 1)
print(matrix_explorer(2, 1) == 1)

##################### q.1.2 ##########################
print(matrix_explorer_memo(3, 2) == 3)
print(matrix_explorer_memo(12, 9) == 75582)
print(matrix_explorer_memo(1, 1) == 1)
print(matrix_explorer_memo(2, 2) == 2)
print(matrix_explorer_memo(1, 2) == 1)
print(matrix_explorer_memo(2, 1) == 1)
print(matrix_explorer_memo(12, 21) == 84672315)