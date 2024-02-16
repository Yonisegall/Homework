import question1 as q1
import question2 as q2


def print_func_name_error(func_name):
    print(f'The Function {func_name} doesnt exist or the name is incorrect')


def q1_get_digits():
    try:
        answer = q1.get_digits_list(5555)
        if type(answer[0]) != int:
            print('The List from function get_digits_list is not made of ints, check its type')
            return False
        if answer != [5, 5, 5, 5]:
            print('The function get_digits_list doesnt work')
            return False
        return True
    except:
        print_func_name_error('q1_get_digits_list')
        return False


def q1_get_num_of_bulls_hits():
    try:
        answer_1 = q1.get_num_of_bulls_hits(1234, 1234)
        answer_2 = q1.get_num_of_bulls_hits(1234, 5678)
        answer_3 = q1.get_num_of_bulls_hits(1234, 1567)
        if answer_1 != [4, 0] or answer_2 != [0, 0] or answer_3 != [1, 0]:
            print('The Function get_num_of_bulls_hits is faulty')
            return False
        return True
    except:
        print_func_name_error('get_num_of_bulls_hits')
        return False


def q2_my_is_upper():
    try:
        if not q2.my_is_upper("ABC! ") or q2.my_is_upper('ABc'):
            print('question 2, my_is_upper function is faulty')
            return False
        return True
    except:
        print_func_name_error('my_is_upper')
        return False


def q2_my_is_lower():
    try:
        if not q2.my_is_lower("abc! ") or q2.my_is_upper('ABc'):
            print('question 2, my_is_lower function is faulty')
            return False
        return True
    except:
        print_func_name_error('my_is_upper')
        return False


def q2_my_upper():
    try:
        if not q2.my_upper('abc !') == 'ABC !':
            print('question 2, my_upper function is faulty')
            return False
        return True
    except:
        print_func_name_error('my_upper')
        return False


def q2_my_lower():
    try:
        if q2.my_lower('ABC !') != 'abc !':
            print('question 2, my_lower function is faulty')
            return False
        return True
    except:
        print_func_name_error('my_lower')
        return False


def q2_string_changer():
    try:
        if q2.string_changer('AaBbCc! $AaBbCc! $AaBbCc! ') != 'aAbBcC! AaBbCc! aAbBcC! ':
            print('function string_changer is faulty')
            return False
        return True
    except:
        print_func_name_error('string_changer')
        return False


def overall(bool_list):
    if False not in bool_list[:2]:
        print('question 1 should work fine')
    if False not in bool_list[2:]:
        print('question 2 should work fine')
    if False not in bool_list:
        print('check maybe the prints are not perfect')


def main():
    # question 1 test
    list_of_flags = []
    list_of_flags.append(q1_get_digits())
    list_of_flags.append(q1_get_num_of_bulls_hits())
    # question 2 test
    list_of_flags.append(q2_my_is_upper())
    list_of_flags.append(q2_my_is_lower())
    list_of_flags.append(q2_my_upper())
    list_of_flags.append(q2_my_lower())
    list_of_flags.append(q2_string_changer())
    overall(list_of_flags)
    return None


if __name__ == '__main__':
    main()
