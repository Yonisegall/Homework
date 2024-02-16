# ************************ HOMEWORK 1 QUESTION 2 **************************
def question2(day, is_rainy):
    ### WRITE CODE HERE
    if day == "sat": # dosen't metter if rainy
        print("Building No. 96")
    else:
        if is_rainy == True: # rainy
            if day == "mon" or day == "wed" or day == "fri":
                print("Student Center")
            else:
                print("Library")
        else: # not rainy.
            if day == "mon" or day == "wed" or day == "fri":
                print("Swimming Pool")
            else:
                print("Rager Gate")









