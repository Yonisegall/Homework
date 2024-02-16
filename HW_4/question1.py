def semi_factorial(num):
    """
    :param: A number.

    :return: Calculation:
             if the number is odd - multiply it by the number below it.
             then multiply the below number with the below number
             until 1 and then, connection every thing together.

    """
    ##Code ##
    if num == 1:
        return 1
    if num % 2 == 0:
        return num + semi_factorial(num-1)
    else:
        return num * (num-1) + semi_factorial(num-2)

################################-Tests-#####################################

########################## Q.1 #################################

print(semi_factorial(1) == 1)
print(semi_factorial(3) == 7)
print(semi_factorial(6) == 33)
print(semi_factorial(2) == 3)
print(semi_factorial(4) == 11)
print(semi_factorial(567) == 30460989)



