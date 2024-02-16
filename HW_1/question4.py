# ************************ HOMEWORK 1 QUESTION 4 **************************
def question4(input_list):
    # ***** WRITE CODE HERE *****
    list_0  = False # if sum_list = 0 or not.
    min_num = 0 # the smallest number in the list
    max_num = 0 # the biggest number in the list.
    sum_list = 0 # addition of the numbers in the list.
    for i in input_list:
        sum_list = sum_list + i
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i
        if sum_list == 0:
            list_0 = True
            break
    if list_0 == True:
        print((min_num + max_num) / 2)  # average of the biggest and smallest number in the list
    else:
        print("error")

