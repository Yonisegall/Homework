def decimal_to_base(dec_num, base_num):
    """
    :param: dec_num - A non-negative integer in 10 base
    :param: base_num - the base that we want to represent
            the number.

    :return: The number in representation with the new base.
    """
    ##Code ##
    result = ""
    return dec_t_ba(dec_num, base_num, result)

def dec_t_ba(dec_num, base_num, result):
    """
     :param: dec_num - A non-negative integer in 10 base
     :param: base_num - the base that we want to represent
     :param: result - empty list that will be the number in representation
              with the new base.

     :return: To the first function the number in representation
              with the new base.
     """
    ##Code ##
    a = str(dec_num % base_num)
    result = a + result
    if dec_num//base_num == 0:
       return result
    return dec_t_ba(dec_num//base_num, base_num, result)



def base_to_decimal(string_to_convert, base_num):
    """
    :param string_to_convert - A number in string
    :param base_num - The base that the number is represented by.

    :return: The number represented on 10 base.
    """
    ##Code ##
    num = 0
    sum_str = len(string_to_convert)
    return bas_t_dec_2(string_to_convert, base_num, num, sum_str)

def bas_t_dec_2(string_to_convert, base_num, num, sum_str):
    """
    :param: string_to_convert - A number in string
    :param: base_num - The base that the number is represented by.
    :param: num - 0. start in 0 and return the number represent by
            10 base.
    :param: sum_str - the len of the digits in the number in the string.

    :return: To the first function - the number represented
             on 10 base.
    """
    if len(string_to_convert) == 0:
        return num
    digit = int(string_to_convert[0])
    num += digit * (base_num ** (sum_str - 1))
    return bas_t_dec_2(string_to_convert[1:], base_num, num, sum_str - 1)




################################-Tests-#####################################

########################## Q.4.1 #################################

# print(decimal_to_base(10,4) == '22')
# print(decimal_to_base(10,5) == '20')
# print(decimal_to_base(10,10) == '10')
# print(decimal_to_base(0,3) == "0")
# print(decimal_to_base(7,3) == "21")
# print(decimal_to_base(4,4) == "10")
# print(decimal_to_base(100,9) == "121")
# print(decimal_to_base(658,2) == "1010010010")
# print(decimal_to_base(658,3) == "220101")
# print(decimal_to_base(23451,8) == "55633")
# print(decimal_to_base(4,9) == "4")
# print(decimal_to_base(0,9) == "0")

########################## Q.4.2 #################################

# print(base_to_decimal("22",4) == 10)
# print(base_to_decimal('20',5) == 10)
# print(base_to_decimal('10', 10) == 10)
# print(base_to_decimal('0',3) == 0)
# print(base_to_decimal('21',3) == 7)
# print(base_to_decimal("10", 4) == 4)
# print(base_to_decimal("121", 9) == 100)
# print(base_to_decimal("", 9) == 0)
# print(base_to_decimal("1010010010",2) == 658)
# print(base_to_decimal("220101",3) == 658)
# print(base_to_decimal("55633",8) == 23451)
# print(base_to_decimal("4",9) == 4)
# print(base_to_decimal("0",9) == 0)
