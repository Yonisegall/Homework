# ************************ QUESTION 2.1 **************************
### WRITE CODE HERE
def my_is_upper(text):
    """
    Arg:
       text from string type.
    return:
        True or False if all the letters in
        the string is capital letters
    """
    for i in text:
        if 123 > ord(i) > 96:
            return False
    return True

def my_is_lower(text):
    """
    Arg:
       text from string type.
    return:
        True or False if all the letters in
        the string is small letters
    """
    for i in text:
        if 91 > ord(i) > 64:
            return False
    return True

# ************************ QUESTION 2.2 **************************
### WRITE CODE HERE
def my_upper(text):
    """
    Arg:
        text from string type.
    return:
        text that all the small letters in the string
        change to capital letters.
    """
    new_text = ""
    new_ord = 0
    for i in range(len(text)):
        if not my_is_upper(text[i]):
            new_ord = ord(text[i]) - 32
            new_text = new_text + chr(new_ord)
        else:
            new_text = new_text + text[i]
    return new_text

def my_lower(text):
    """
   Arg:
       text from string type.
   return:
       text that all the capital letters in the string
       change to small letters.
   """
    new_text = ""
    new_ord = 0
    for i in range(len(text)):
        if not my_is_lower(text[i]):
            new_ord = ord(text[i]) + 32
            new_text = new_text + chr(new_ord)
        else:
            new_text = new_text + text[i]
    return new_text

# ************************ QUESTION 2.3 **************************
### WRITE CODE HERE
def string_changer(text):
    """
   Arg:
       text from string type.
   return:
       text that all the small letters and the capital
       letters, is replaced.
       if there is "$" note in the string,
       after "$" even times  - change
       after "$" odd times - not change
   """
    new_text = ""
    bool_1 = True
    for i in text:
        if i == "$":
            bool_1 = not bool_1
            continue
        if bool_1 == True:
            if my_is_upper(i) == True:
                new_text = new_text + my_lower(i)
            else:
                new_text = new_text + my_upper(i)
        else:
            new_text += i
    return new_text
