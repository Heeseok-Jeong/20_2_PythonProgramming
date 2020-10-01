#Import sys to use sys.exit()
import sys

#Show user what is the program and how to use it
print("---------------------------------------------------------------")
print("Welcome, this is JHS's unit converter :)")
print("There are 7 main functions and they have sub-menu.")
print("You can put an appropriate number to use a function what you want(as well as sub-menu).")
print("Let's get it!")
print("---------------------------------------------------------------\n")

#Show user what main functions exist
print("Main functions")
print("1. Length Converter")
print("2. Mass Converter")
print("3. Currency Converter")
print("4. Frequency Converter")
print("5. Temperature Converter")
print("6. Data Storage Converter")
print("7. Time Converter")

#create variables
num_convert = ""
scale_before = ""
scale_after = ""
result = 0

#Get a function number user want to use, 1~7
num_func = input("Which converter do you want?(1~7) : ")
#check the string is empty
if num_func == '':
    #print what's wrong
    print("Error : You put an empty value!")
    #show user to put enter key to quit the program
    print("Please enter to quit the program.")
    #wait until get enter
    input()
    #then, quit the program
    sys.exit()
#change string to int, check the number isn't numeric value
try:
    #if the input isn't numeric value by chaning string to int
    num_func = int(num_func)
#print what's wrong
except(ValueError):
    print("Error : You put a non-numeric value!")
    #show user to put enter key to quit the program
    print("Please enter to quit the program.")
    #wait until get enter
    input()
    #then, quit the program
    sys.exit()
#check the number is out of range
if not 1<=num_func<=7:
    #print what's wrong
    print("Error : You put an out of ranged value!")
    #show user to put enter key to quit the program
    print("Please enter to quit the program.")
    #wait until get enter
    input()
    #then, quit the program
    sys.exit()

#Length Converter function
if num_func == 1:
    #Show user what function chose
    print("\nLength Converter!\n")
    #Show user what sub-menu of Length Converter exist
    print("Sub-Menu")
    print("1-1. CentiMeters -> MilliMeters")
    print("1-2. Meters -> CentiMeters")
    print("1-3. KiloMeters -> Meters")
    #Get a sub-menu number user want to use
    num_sub = input("Which sub-menu do you want?(1~3) : ")
    #check the string is empty
    if num_sub == '':
        #print what's wrong
        print("Error : You put an empty value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()
    #change string to int, check the number isn't numeric value
    try:
        #if the input isn't numeric value by chaning string to int
        num_sub = int(num_sub)
    #print what's wrong
    except(ValueError):
        print("Error : You put a non-numeric value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()
    #check the number is out of range
    if not 1<=num_sub<=3:
        #print what's wrong
        print("Error : You put an out of ranged value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()
    # #Check the sub-menu number is valid and get the string->int
    # num_sub = check_valid_num(num_sub, 1, 3)

    #CentiMeters -> MilliMeters mode
    if num_sub == 1:
        print("\nCentiMeters -> MilliMeters!\n")
        #set scale_before
        scale_before = "CentiMeters"
        #set scale_after
        scale_after = "MilliMeters"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()

        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()

        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        # #Check the sub-menu number is valid and get the string->int
        # num_convert = check_valid_num_convert(num_convert)

        #convert num_convert CentiMeters to proper MilliMeters
        result = num_convert*10
    #Meters -> CentiMeters mode
    elif num_sub == 2:
        print("\nMeters -> CentiMeters!\n")
        #set scale_before
        scale_before = "Meters"
        #set scale_after
        scale_after = "CentiMeters"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert Meters to proper CentiMeters
        result = num_convert*100
    #KiloMeters -> Meters mode
    elif num_sub == 3:
        print("\nKiloMeters -> Meters!\n")
        #set scale_before
        scale_before = "KiloMeters"
        #set scale_after
        scale_after = "Meters"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert KiloMeters to proper Meters
        result = num_convert*1000

#Mass Converter function
elif num_func == 2:
    #Show user what function chose
    print("\nMass Converter!\n")
    #Show user what sub-menu of Mass Converter exist
    print("Sub-Menu")
    print("2-1. Gram -> MilliGram")
    print("2-2. KiloGram -> Gram")
    print("2-3. Tonne -> KiloGram")

    #Get a sub-menu number user want to use
    num_sub = input("Which sub-menu do you want?(1~3) : ")
    #check the string is empty
    if num_sub == '':
        #print what's wrong
        print("Error : You put an empty value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()
    #change string to int, check the number isn't numeric value
    try:
        #if the input isn't numeric value by chaning string to int
        num_sub = int(num_sub)
    #print what's wrong
    except(ValueError):
        print("Error : You put a non-numeric value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()
    #check the number is out of range
    if not 1<=num_sub<=3:
        #print what's wrong
        print("Error : You put an out of ranged value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()

    #Gram -> MilliGram mode
    if num_sub == 1:
        print("\nGram -> MilliGram!\n")
        #set scale_before
        scale_before = "Gram"
        #set scale_after
        scale_after = "MilliGram"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert Gram to proper MilliGram
        result = num_convert*1000
    #KiloGram -> Gram mode
    elif num_sub == 2:
        print("\nKiloGram -> Gram!\n")
        #set scale_before
        scale_before = "KiloGram"
        #set scale_after
        scale_after = "Gram"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert KiloGram to proper Gram
        result = num_convert*1000
    #Tonne -> KiloGram mode
    elif num_sub == 3:
        print("\nTonne -> KiloGram!\n")
        #set scale_before
        scale_before = "Tonne"
        #set scale_after
        scale_after = "KiloGram"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert Tonne to proper KiloGram
        result = num_convert*1000
#Currency Converter function
elif num_func == 3:
    #Show user what function chose
    print("\nCurrency Converter!\n")
    #Show user what sub-menu of Currency Converter exist
    print("Sub-Menu")
    print("3-1. Dollars -> Won")
    print("3-2. Yen -> Won")
    print("3-3. Yuan -> Won")

    #Get a sub-menu number user want to use
    num_sub = input("Which sub-menu do you want?(1~3) : ")
    #check the string is empty
    if num_sub == '':
        #print what's wrong
        print("Error : You put an empty value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()
    #change string to int, check the number isn't numeric value
    try:
        #if the input isn't numeric value by chaning string to int
        num_sub = int(num_sub)
    #print what's wrong
    except(ValueError):
        print("Error : You put a non-numeric value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()
    #check the number is out of range
    if not 1<=num_sub<=3:
        #print what's wrong
        print("Error : You put an out of ranged value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()

    #Dollars -> Won mode
    if num_sub == 1:
        print("\nDollars -> Won!\n")
        #set scale_before
        scale_before = "Dollars"
        #set scale_after
        scale_after = "Won"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert Dollars to proper Won
        result = num_convert*1200
    #Yen -> Won mode
    elif num_sub == 2:
        print("\nYen -> Won!\n")
        #set scale_before
        scale_before = "Yen"
        #set scale_after
        scale_after = "Won"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert Yen to proper Won
        result = num_convert*11
    #Yuan -> Won mode
    elif num_sub == 3:
        print("\nYuan -> Won!\n")
        #set scale_before
        scale_before = "Yuan"
        #set scale_after
        scale_after = "Won"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert Yuan to proper Won
        result = num_convert*170
#Frequency Converter function
elif num_func == 4:
    #Show user what function chose
    print("\nFrequency Converter!\n")
    #Show user what sub-menu of Frequency Converter exist
    print("Sub-Menu")
    print("4-1. KiloHertz -> Hertz")
    print("4-2. MegaHertz -> KiloHertz")
    print("4-3. GigaHertz -> MegaHertz")

    #Get a sub-menu number user want to use
    num_sub = input("Which sub-menu do you want?(1~3) : ")
    #check the string is empty
    if num_sub == '':
        #print what's wrong
        print("Error : You put an empty value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()
    #change string to int, check the number isn't numeric value
    try:
        #if the input isn't numeric value by chaning string to int
        num_sub = int(num_sub)
    #print what's wrong
    except(ValueError):
        print("Error : You put a non-numeric value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()
    #check the number is out of range
    if not 1<=num_sub<=3:
        #print what's wrong
        print("Error : You put an out of ranged value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()

    #Hertz -> KiloHertz mode
    if num_sub == 1:
        print("\nKiloHertz -> Hertz!\n")
        #set scale_before
        scale_before = "KiloHertz"
        #set scale_after
        scale_after = "Hertz"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert KiloHertz to proper Hertz
        result = num_convert*1000
    #MegaHertz -> KiloHertz mode
    elif num_sub == 2:
        print("\nMegaHertz -> KiloHertz!\n")
        #set scale_before
        scale_before = "MegaHertz"
        #set scale_after
        scale_after = "KiloHertz"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert MegaHertz to proper KiloHertz
        result = num_convert*1000
    #GigaHertz -> MegaHertz mode
    elif num_sub == 3:
        print("\nGigaHertz -> MegaHertz!\n")
        #set scale_before
        scale_before = "GigaHertz"
        #set scale_after
        scale_after = "MegaHertz"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert GigaHertz to proper MegaHertz
        result = num_convert*1000
#Temperature Converter function
elif num_func == 5:
    #Show user what function chose
    print("\nTemperature Converter!\n")
    #Show user what sub-menu of Temperature Converter exist
    print("Sub-Menu")
    print("5-1. Fahrenheit -> Celsius")
    print("5-2. Celsius -> Fahrenheit")
    print("5-3. Kelvin -> Celsius")
    print("5-4. Celsius -> Kelvin")

    #Get a sub-menu number user want to use
    num_sub = input("Which sub-menu do you want?(1~4) : ")
    #check the string is empty
    if num_sub == '':
        #print what's wrong
        print("Error : You put an empty value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()
    #change string to int, check the number isn't numeric value
    try:
        #if the input isn't numeric value by chaning string to int
        num_sub = int(num_sub)
    #print what's wrong
    except(ValueError):
        print("Error : You put a non-numeric value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()
    #check the number is out of range
    if not 1<=num_sub<=4:
        #print what's wrong
        print("Error : You put an out of ranged value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()

    #Fahrenheit -> Celsius mode
    if num_sub == 1:
        print("\nFahrenheit -> Celsius!\n")
        #set scale_before
        scale_before = "Fahrenheit"
        #set scale_after
        scale_after = "Celsius"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert Fahrenheit to proper Celsius
        result = (num_convert-32)*5/9
    #Celsius -> Fahrenheit mode
    elif num_sub == 2:
        print("\nCelsius -> Fahrenheit!\n")
        #set scale_before
        scale_before = "Celsius"
        #set scale_after
        scale_after = "Fahrenheit"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert Celsius to proper Fahrenheit
        result = (num_convert*9/5)+32
    #Kelvin -> Celsius mode
    elif num_sub == 3:
        print("\nKelvin -> Celsius!\n")
        #set scale_before
        scale_before = "Kelvin"
        #set scale_after
        scale_after = "Celsius"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert Kelvin to proper Celsius
        result = num_convert-273.15
    #Celsius -> Kelvin mode
    elif num_sub == 4:
        print("\nCelsius -> Kelvin!\n")
        #set scale_before
        scale_before = "Celsius"
        #set scale_after
        scale_after = "Kelvin"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert Celsius to proper Kelvin
        result = num_convert+273.15
#Data Storage Converter function
elif num_func == 6:
    #Show user what function chose
    print("\nData Storage Converter!\n")
    #Show user what sub-menu of Data Storage Converter exist
    print("Sub-Menu")
    print("6-1. Byte -> Bit")
    print("6-2. MegaByte -> Byte")
    print("6-3. GigaByte -> MegaByte")

    #Get a sub-menu number user want to use
    num_sub = input("Which sub-menu do you want?(1~3) : ")
    #check the string is empty
    if num_sub == '':
        #print what's wrong
        print("Error : You put an empty value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()
    #change string to int, check the number isn't numeric value
    try:
        #if the input isn't numeric value by chaning string to int
        num_sub = int(num_sub)
    #print what's wrong
    except(ValueError):
        print("Error : You put a non-numeric value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()
    #check the number is out of range
    if not 1<=num_sub<=3:
        #print what's wrong
        print("Error : You put an out of ranged value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()

    #Byte -> Byte mode
    if num_sub == 1:
        print("\nByte -> Bit!\n")
        #set scale_before
        scale_before = "Byte"
        #set scale_after
        scale_after = "Bit"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert Byte to proper Bit
        result = num_convert*8
    #MegaByte -> Byte mode
    elif num_sub == 2:
        print("\nMegaByte -> Byte!\n")
        #set scale_before
        scale_before = "MegaByte"
        #set scale_after
        scale_after = "Byte"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert MegaByte to proper Byte
        result = num_convert*1000000
    #GigaByte -> MegaByte mode
    elif num_sub == 3:
        print("\nGigaByte -> MegaByte!\n")
        #set scale_before
        scale_before = "GigaByte"
        #set scale_after
        scale_after = "MegaByte"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert GigaByte to proper MegaByte
        result = num_convert*1000
#Time Converter function
elif num_func == 7:
    #Show user what function chose
    print("\nTime Converter!\n")
    #Show user what sub-menu of Time Converter exist
    print("Sub-Menu")
    print("7-1. Year -> Month")
    print("7-2. Year -> Week")
    print("7-3. Year -> Day")

    #Get a sub-menu number user want to use
    num_sub = input("Which sub-menu do you want?(1~3) : ")
    #check the string is empty
    if num_sub == '':
        #print what's wrong
        print("Error : You put an empty value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()
    #change string to int, check the number isn't numeric value
    try:
        #if the input isn't numeric value by chaning string to int
        num_sub = int(num_sub)
    #print what's wrong
    except(ValueError):
        print("Error : You put a non-numeric value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()
    #check the number is out of range
    if not 1<=num_sub<=3:
        #print what's wrong
        print("Error : You put an out of ranged value!")
        #show user to put enter key to quit the program
        print("Please enter to quit the program.")
        #wait until get enter
        input()
        #then, quit the program
        sys.exit()

    #Year -> Month mode
    if num_sub == 1:
        print("\nYear -> Month!\n")
        #set scale_before
        scale_before = "Year"
        #set scale_after
        scale_after = "Month"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert Year to proper Month
        result = num_convert*12
    #Year -> Week mode
    elif num_sub == 2:
        print("\nYear -> Week!\n")
        #set scale_before
        scale_before = "Year"
        #set scale_after
        scale_after = "Week"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert Year to proper Week
        result = num_convert*52.143
    #Year -> Day mode
    elif num_sub == 3:
        print("\nYear -> Day!\n")
        #set scale_before
        scale_before = "Year"
        #set scale_after
        scale_after = "Day"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #check the string is empty
        if num_convert == '':
            #print what's wrong
            print("Error : You put an empty value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the string contains dot to distinguish it is float type, only positive integer allowed
        if '.' in num_convert:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #change string to int, check the number isn't numeric value
        try:
            #if the input isn't numeric value by chaning string to int
            num_convert = int(num_convert)
        #print what's wrong
        except(ValueError):
            print("Error : You put a non-numeric value!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #check the number is out of range, only positive integer allowed
        if num_convert<1:
            #print what's wrong
            print("Error : You didn't put a positive integer!")
            #show user to put enter key to quit the program
            print("Please enter to quit the program.")
            #wait until get enter
            input()
            #then, quit the program
            sys.exit()
        #convert num_convert Year to proper Day
        result = num_convert*365

#print result to the second decimal point
print("\nResult :", num_convert, scale_before, "-> ", '%.2f' % result, scale_after)
