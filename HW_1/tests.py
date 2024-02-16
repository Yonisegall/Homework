import question1
import question2
import question3
import question4


def test_question1():
    radius = 1  # Change me!
    height = 5  # Change me!
    question1.question1(radius, height)


def test_question2():
    day = 'sun'  # Change me!
    is_rainy = False  # Change me!
    question2.question2(day, is_rainy)


def test_question3():
    input_num = 3  # Change me!
    question3.question3(input_num)


def test_question4():
    input_list = [-1 , -5, 4, 2 , 9]  # Change me!
    question4.question4(input_list)


if __name__ == '__main__':
    test_question1()
    test_question2()
    test_question3()
    test_question4()
