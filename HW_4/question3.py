def longest_super_subsequence(input_list):
    """
    The function gets list of integers and return "super sequence". There is
    super sequence if the next number in the list greater than the sum
    of all the numbers before it. The function return the length of the
    longest super sequence in the list.
    :arg: List.

    :return: The longest super sequence in the list.
    """
    ##Code ##
    count = 0
    if len(input_list) == 0:
        return 0
    sum_list = input_list[0]
    n = 0
    return long_sup_sub_2(input_list, count, sum_list, n)

def long_sup_sub_2(input_list, count, sum_list, n):
    """
    :param: input_list - The list from the first function.
    :param: count - the len of the super sequence.
    :param: sum_list - start with the first organ. Add all the elements together.
    :param: n - start with the first number in the list and
            goes through all the elements in the list

    :return: The length of the longest count.
    """
    ##Code ##
    if n == len(input_list):
        return count
    if input_list[n] >= sum_list:
        if n == 0:
            sum_list = 0
        option_1 = long_sup_sub_2(input_list, count + 1, sum_list + input_list[n], n + 1)
        option_2 = long_sup_sub_2(input_list, count, sum_list, n + 1)
        if option_1 >= option_2:
            return option_1
        else:
            return option_2
    else:
        return long_sup_sub_2(input_list, count, sum_list, n + 1)
################################-Tests-#####################################

########################## Q.3 #################################

print(longest_super_subsequence([0,3,6,9,11]) == 4)
print(longest_super_subsequence([22,23,24,25,26,27]) == 2)
print(longest_super_subsequence([1,1,1]) == 2)
print(longest_super_subsequence([-5,-4,-8]) == 3)
print(longest_super_subsequence([3,6,9,20,0,1,2,3,7,40]) == 6)
print(longest_super_subsequence([-20,-19,-18,-17]) == 4)
print(longest_super_subsequence([0,0,-1,0,-1,0 ,0]) == 5)
print(longest_super_subsequence([1,2,20,5,10]) == 4)
print(longest_super_subsequence([0,1,3,2,3,6]) == 5)
print(longest_super_subsequence([]) == 0)
print(longest_super_subsequence([-1,-9,0,3,6,9,11]) == 6)







