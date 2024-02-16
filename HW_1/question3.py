# ************************ HOMEWORK 1 QUESTION 3 **************************
def question3(input_num):
    ### WRITE CODE HERE
    num_t = 1 # number of times that "input_num" will be printed.
    while 1 <= input_num <= 9:
        print(str(input_num) * num_t) # input_num to "string" for printing several times.
        input_num = input_num - 1
        num_t = num_t + 1

question3(7)

