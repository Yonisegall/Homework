# ************************ QUESTION 1.1 **************************
### WRITE CODE HERE
def get_digits_list(num):
    """
    Arg:
        A number.
    Returns:
        Convert the number to list.
    """
    new_list = []
    for i in str(num):
        i = int(i)
        new_list.append(i)
    return new_list

# ************************ QUESTION 1.2 **************************
### WRITE CODE HERE
def get_num_of_bulls_hits(num, guess):
    """
    Args:
        Number and guess.
    Returns:
        How many bulls and hits the guess in the number.
    """
    num = get_digits_list(num)
    guess = get_digits_list(guess)
    bulls = 0
    hits = 0
    for i in range(len(guess)):
        if num[i] == guess[i]:
            bulls += 1
        elif guess[i] in num:
            hits += 1
    return [bulls, hits]

# ************************ QUESTION 1.3 **************************
## DO NOT CHANGE THE FOLLOWING CODE!
# Import required module
import random
def no_duplicates_checker(num):
    """
    Args:
         A number.
    Returns:
        Boolean: True if the number has no duplicate digit; otherwise False.
    """
    num_li = get_digits_list(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False

def generate_num():
    """ Generate a 4 digits number with no repeated digits
    Return:
         the number
    """
    while True:
        num = random.randint(1000, 9999)
        if no_duplicates_checker(num):
            return num

def play(num=0):
    """ A Bulls and hit game function.
    It gets input from user and print to the user the results.
    Args:
        num [int]: for debugging.
    """
    print("Hello and welcome to Bulls And Hits game!")
    # Secret Code
    if num == 0:
        num = generate_num()
    tries = int(input('Enter number of tries: '))
    ### WRITE CODE HERE
    for i in range(tries):
        guess = int(input("Enter your guess: "))
        result = get_num_of_bulls_hits(num, guess)
        bulls = result[0]
        hits = result[1]
        print(bulls, "bulls,", hits, "hits")
        if bulls == 4 and hits == 0:
            print("You guessed right!")
            return
    print("You ran out of tries. The number was", num)

play()


