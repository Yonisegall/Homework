import question1 as q1
import question2 as q2

################# QUESTION 1 TESTS #################
def test_1a_1():
    return q1.get_digits_list(12345) == [1,2,3,4,5]

def test_1a_2():
    return q1.get_digits_list(1) == [1]


def run_tests_1a():
    print("Tests for question 1a:")
    print("Test 1:", test_1a_1())
    print("Test 2:", test_1a_2())


def test_1b_1():
    return q1.get_num_of_bulls_hits(4012, 4102) == [2,2]


def test_1b_2():
    return q1.get_num_of_bulls_hits(1234, 1234) == [4,0]


def run_tests_1b():
    print("Tests for question 1b:")
    print("Test 1:", test_1b_1())
    print("Test 2:", test_1b_2())

run_tests_1a()
run_tests_1b()

################# QUESTION 2 TESTS #################
def test_2a_1():
    return q2.my_is_upper("a") == False

def test_2a_2():
    return q2.my_is_upper("A") == True

def test_2a_3():
    return q2.my_is_upper("z") == False

def test_2a_4():
    return q2.my_is_upper("Z") == True

def test_2a_5():
    return q2.my_is_upper("aZ") == False

def test_2a_6():
    return q2.my_is_upper("Za") == False

def test_2a_7():
    return q2.my_is_upper("a.") == False

def test_2a_8():
    return q2.my_is_upper("a.z") == False

def test_2a_9():
    return q2.my_is_upper("A.Z") == True

def test_2a_10():
    return q2.my_is_upper("Z.a") == False

def test_2a_11():
    return q2.my_is_upper(".a") == False

def test_2a_12():
    return q2.my_is_upper(".Z") == True

def test_2a_13():
    return q2.my_is_lower("a") == True

def test_2a_14():
    return q2.my_is_lower("A") == False

def test_2a_15():
    return q2.my_is_lower("z") == True

def test_2a_16():
    return q2.my_is_lower("Z") == False

def test_2a_17():
    return q2.my_is_lower("aZ") == False

def test_2a_18():
    return q2.my_is_lower("Za") == False

def test_2a_19():
    return q2.my_is_lower("a.") == True

def test_2a_20():
    return q2.my_is_lower("a.z") == True

def test_2a_21():
    return q2.my_is_lower("A.Z") == False

def test_2a_22():
    return q2.my_is_lower("Z.a") == False

def test_2a_23():
    return q2.my_is_lower(".a") == True

def test_2a_24():
    return q2.my_is_lower(".Z") == False

def run_tests_2a():
    print("Tests for Question 2A:\r\nTests for is_upper:")
    print("Test 1:", test_2a_1())
    print("Test 2:", test_2a_2())
    print("Test 3:", test_2a_3())
    print("Test 4:", test_2a_4())
    print("Test 5:", test_2a_5())
    print("Test 6:", test_2a_6())
    print("Test 7:", test_2a_7())
    print("Test 8:", test_2a_8())
    print("Test 9:", test_2a_9())
    print("Test 10:", test_2a_10())
    print("Test 11:", test_2a_11())
    print("Test 12:", test_2a_12())
    print("Tests for is_lower:")
    print("Test 13:", test_2a_13())
    print("Test 14:", test_2a_14())
    print("Test 15:", test_2a_15())
    print("Test 16:", test_2a_16())
    print("Test 17:", test_2a_17())
    print("Test 18:", test_2a_18())
    print("Test 19:", test_2a_19())
    print("Test 20:", test_2a_20())
    print("Test 21:", test_2a_21())
    print("Test 22:", test_2a_22())
    print("Test 23:", test_2a_23())
    print("Test 24:", test_2a_24())


def test_2b_1():
    return q2.my_upper("A") == "A"


def test_2b_2():
    return q2.my_upper("Z") == "Z"


def test_2b_3():
    return q2.my_upper("a") == "A"


def test_2b_4():
    return q2.my_upper("z") == "Z"


def test_2b_5():
    return q2.my_upper(".") == "."


def test_2b_6():
    return q2.my_upper("Az") == "AZ"


def test_2b_7():
    return q2.my_upper("aZ") == "AZ"


def test_2b_8():
    return q2.my_upper("A.Z") == "A.Z"


def test_2b_9():
    return q2.my_upper("a.z") == "A.Z"


def test_2b_10():
    return q2.my_upper("A.z") == "A.Z"


def test_2b_11():
    return q2.my_upper("I love Pizza") == "I LOVE PIZZA"


def test_2b_12():
    return q2.my_lower("A") == "a"


def test_2b_13():
    return q2.my_lower("Z") == "z"


def test_2b_14():
    return q2.my_lower("a") == "a"


def test_2b_15():
    return q2.my_lower("z") == "z"


def test_2b_16():
    return q2.my_lower(".") == "."


def test_2b_17():
    return q2.my_lower("Az") == "az"


def test_2b_18():
    return q2.my_lower("aZ") == "az"


def test_2b_19():
    return q2.my_lower("A.Z") == "a.z"


def test_2b_20():
    return q2.my_lower("a.z") == "a.z"


def test_2b_21():
    return q2.my_lower("A.z") == "a.z"


def test_2b_22():
    return q2.my_lower("I love Pizza") == "i love pizza"


def run_tests_2b():
    print("Tests for question 2b:\r\nTests for my_upper:")
    print("Test 1:", test_2b_1())
    print("Test 2:", test_2b_2())
    print("Test 3:", test_2b_3())
    print("Test 4:", test_2b_4())
    print("Test 5:", test_2b_5())
    print("Test 6:", test_2b_6())
    print("Test 7:", test_2b_7())
    print("Test 8:", test_2b_8())
    print("Test 9:", test_2b_9())
    print("Test 10:", test_2b_10())
    print("Test 11:", test_2b_11())
    print("Tests for my_lower:")
    print("Test 12:", test_2b_12())
    print("Test 13:", test_2b_13())
    print("Test 14:", test_2b_14())
    print("Test 15:", test_2b_15())
    print("Test 16:", test_2b_16())
    print("Test 17:", test_2b_17())
    print("Test 18:", test_2b_18())
    print("Test 19:", test_2b_19())
    print("Test 20:", test_2b_20())
    print("Test 21:", test_2b_21())
    print("Test 22:", test_2b_22())


def test_2c_1():
    return q2.string_changer("H") == "h"


def test_2c_2():
    return q2.string_changer("a") == "A"


def test_2c_3():
    return q2.string_changer(" ") == " "


def test_2c_4():
    return q2.string_changer("$") == ""


def test_2c_5():
    return q2.string_changer("Ha") == "hA"


def test_2c_6():
    return q2.string_changer("aH") == "Ah"


def test_2c_7():
    return q2.string_changer("H$") == "h"


def test_2c_8():
    return q2.string_changer("H$a") == "ha"


def test_2c_9():
    return q2.string_changer("H$a$B") == "hab"


def test_2c_10():
    return q2.string_changer("H$$r") == "hR"


def run_tests_2c():
    print("Tests for question 2c:")
    print("Test 1:", test_2c_1())
    print("Test 2:", test_2c_2())
    print("Test 3:", test_2c_3())
    print("Test 4:", test_2c_4())
    print("Test 5:", test_2c_5())
    print("Test 6:", test_2c_6())
    print("Test 7:", test_2c_7())
    print("Test 8:", test_2c_8())
    print("Test 9:", test_2c_9())
    print("Test 10:", test_2c_10())


run_tests_2a()
run_tests_2b()
run_tests_2c()


