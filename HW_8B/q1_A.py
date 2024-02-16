###################################### ---Q1A--- ######################################
from Stack import *
from DNA import *


def sort_DNA_Stack(DNA_stack):
    """
    The function receives a stack-type data structure, which contains DNA objects, and sorts them based on the
    length and their mass. The first criterion for sorting will be the length of the DNA, when the lengths of the DNA
    are the same, the order is determined according to the mass. The function will return a new array sorted, so that
    the largest DNA (according to the defined criteria) will be at the top the cartridge.

    :param DNA_stack: A stack
    :return: Sorted stack.
    """
    sorted_stack = Stack()
    temp = DNA_stack.pop()
    while not DNA_stack.is_empty():
        if sorted_stack.is_empty():
            sorted_stack.push(temp)
            temp = DNA_stack.pop()
        if len(temp) > len(sorted_stack.peek()):
            (temp, DNA_stack, sorted_stack) = Internal_sort(temp, DNA_stack, sorted_stack)
        elif len(temp) == len(sorted_stack.peek()):
            if temp.calculate_mass() > sorted_stack.peek().calculate_mass():
                (temp, DNA_stack, sorted_stack) = Internal_sort(temp, DNA_stack, sorted_stack)
            else:
                DNA_stack.push(sorted_stack.pop())
        else:
            DNA_stack.push(sorted_stack.pop())
    sorted_stack.push(temp)
    return sorted_stack


def Internal_sort(temp, DNA_stack, sorted_stack):
    """ The function returns all arguments after internal sorting """
    if len(temp) < len(DNA_stack.peek()):
        sorted_stack.push(temp)
        temp = DNA_stack.pop()
    elif len(temp) == len(DNA_stack.peek()):
        if temp.calculate_mass() < DNA_stack.peek().calculate_mass():
            sorted_stack.push(temp)
            temp = DNA_stack.pop()
        else:
            sorted_stack.push(temp)
            temp = DNA_stack.pop()
            DNA_stack.push(sorted_stack.pop())
    else:
        sorted_stack.push(temp)
        temp = DNA_stack.pop()
        DNA_stack.push(sorted_stack.pop())
    return temp, DNA_stack, sorted_stack


########### Tests ############
stack_1 = Stack()
stack_1.push(DNA("TGGGTA"))
stack_1.push(DNA("ATGGAA"))
stack_1.push(DNA("AGTCAAAGGGCTTTATATAT"))
stack_1.push(DNA("AGGGGGGCCCCCC"))
stack_1.push(DNA("AGGGGGCCC"))
print(f"The original DNA stack:")
print(stack_1)
print("Sorted DNA are: ")
sortedst = sort_DNA_Stack(stack_1)
print(sortedst)

ck_1 = Stack()
ck_1.push(DNA("AAA"))
ck_1.push(DNA("GGGGG"))
ck_1.push(DNA("AAC"))
ck_1.push(DNA("AAAAAA"))
print(ck_1)
print("Sorted DNA are: ")
sortedst = sort_DNA_Stack(ck_1)
print(sortedst)
