#Import sys to use sys.exit()
import sys

##Get enter from user to quit the program and quit this program
def terminate():
    #show user to put enter key to quit the program
    print("Please enter to quit the program.")
    #wait until get enter
    input()
    #then, quit the program
    sys.exit()

##Check num_func and num_sub are valid and return that number
def check_valid_num(num, range_from, range_to):
    #check the number is empty
    if num == '':
        #print what's wrong
        print("Error : You put an empty value!")
        #go to terminate condition
        terminate()

    #check the number isn't numeric value
    try:
        #if the input isn't numeric value
        num = int(num)
    #print what's wrong
    except(ValueError):
        print("Error : You put a non-numeric value!")
        #go to terminate condition
        terminate()

    #check the number is out of range
    if not range_from<=num<=range_to:
        #print what's wrong
        print("Error : You put an out of ranged value!")
        #go to terminate condition
        terminate()

    return num

##Check num_convert is valid and return that float number
def check_valid_num_convert(num):
    #check the number is empty
    if num == '':
        #print what's wrong
        print("Error : You put an empty value!")
        #go to terminate condition
        terminate()

    #check the number isn't numeric value
    try:
        #if the input isn't numeric value
        num = float(num)
    #print what's wrong
    except(ValueError):
        print("Error : You put a non-numeric value!")
        #go to terminate condition
        terminate()

    #check the number is out of range
    if num<1:
        #print what's wrong
        print("Error : You didn't put a positive integer!")
        #go to terminate condition
        terminate()

    return num

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

#Get a function number user want to use, 1~7
num_func = input("Which converter do you want?(1~7) : ")
#Check the function number is valid and get the string->number
num_func = check_valid_num(num_func, 1, 7)

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
    #Check the sub-menu number is valid and get the string->number
    num_sub = check_valid_num(num_sub, 1, 3)

    #CentiMeters -> MilliMeters mode
    if num_sub == 1:
        print("\nCentiMeters -> MilliMeters!\n")
        #set scale_before
        scale_before = "CentiMeters"
        #set scale_after
        scale_after = "MilliMeters"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet CentiMeters to proper MilliMeters
        result = num_convet*10
    #Meters -> CentiMeters mode
    elif num_sub == 2:
        print("\nMeters -> CentiMeters!\n")
        #set scale_before
        scale_before = "Meters"
        #set scale_after
        scale_after = "CentiMeters"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet Meters to proper CentiMeters
        result = num_convet*100
    #KiloCentis -> Meters mode
    elif num_sub == 3:
        print("\nKiloCentis -> Meters!\n")
        #set scale_before
        scale_before = "KiloMeters"
        #set scale_after
        scale_after = "Meters"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet KiloMeters to proper Meters
        result = num_convet*1000
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
    #Check the sub-menu number is valid and get the string->number
    num_sub = check_valid_num(num_sub, 1, 3)

    #Gram -> MilliGram mode
    if num_sub == 1:
        print("\nGram -> MilliGram!\n")
        #set scale_before
        scale_before = "Gram"
        #set scale_after
        scale_after = "MilliGram"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet Gram to proper MilliGram
        result = num_convet*1000
    #KiloGram -> Gram mode
    elif num_sub == 2:
        print("\nKiloGram -> Gram!\n")
        #set scale_before
        scale_before = "KiloGram"
        #set scale_after
        scale_after = "Gram"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet KiloGram to proper Gram
        result = num_convet*1000
    #Tonne -> KiloGram mode
    elif num_sub == 3:
        print("\nTonne -> KiloGram!\n")
        #set scale_before
        scale_before = "Tonne"
        #set scale_after
        scale_after = "KiloGram"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet Tonne to proper KiloGram
        result = num_convet*1000
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
    #Check the sub-menu number is valid and get the string->number
    num_sub = check_valid_num(num_sub, 1, 3)

    #Dollars -> Won mode
    if num_sub == 1:
        print("\nDollars -> Won!\n")
        #set scale_before
        scale_before = "Dollars"
        #set scale_after
        scale_after = "Won"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet Dollars to proper Won
        result = num_convet*1200
    #Yen -> Won mode
    elif num_sub == 2:
        print("\nYen -> Won!\n")
        #set scale_before
        scale_before = "Yen"
        #set scale_after
        scale_after = "Won"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet Yen to proper Won
        result = num_convet*11
    #Yuan -> Won mode
    elif num_sub == 3:
        print("\nYuan -> Won!\n")
        #set scale_before
        scale_before = "Yuan"
        #set scale_after
        scale_after = "Won"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet Yuan to proper Won
        result = num_convet*170
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
    #Check the sub-menu number is valid and get the string->number
    num_sub = check_valid_num(num_sub, 1, 3)

    #Hertz -> KiloHertz mode
    if num_sub == 1:
        print("\nKiloHertz -> Hertz!\n")
        #set scale_before
        scale_before = "KiloHertz"
        #set scale_after
        scale_after = "Hertz"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet KiloHertz to proper Hertz
        result = num_convet*1000
    #MegaHertz -> KiloHertz mode
    elif num_sub == 2:
        print("\nMegaHertz -> KiloHertz!\n")
        #set scale_before
        scale_before = "MegaHertz"
        #set scale_after
        scale_after = "KiloHertz"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet MegaHertz to proper KiloHertz
        result = num_convet*1000
    #GigaHertz -> MegaHertz mode
    elif num_sub == 3:
        print("\nGigaHertz -> MegaHertz!\n")
        #set scale_before
        scale_before = "GigaHertz"
        #set scale_after
        scale_after = "MegaHertz"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet GigaHertz to proper MegaHertz
        result = num_convet*1000
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
    #Check the sub-menu number is valid and get the string->number
    num_sub = check_valid_num(num_sub, 1, 4)

    #Fahrenheit -> Celsius mode
    if num_sub == 1:
        print("\nFahrenheit -> Celsius!\n")
        #set scale_before
        scale_before = "Fahrenheit"
        #set scale_after
        scale_after = "Celsius"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet Fahrenheit to proper Celsius
        result = (num_convet-32)*5/9
    #Celsius -> Fahrenheit mode
    elif num_sub == 2:
        print("\nCelsius -> Fahrenheit!\n")
        #set scale_before
        scale_before = "Celsius"
        #set scale_after
        scale_after = "Fahrenheit"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet Celsius to proper Fahrenheit
        result = (num_convet*9/5)+32
    #Kelvin -> Celsius mode
    elif num_sub == 3:
        print("\nKelvin -> Celsius!\n")
        #set scale_before
        scale_before = "Kelvin"
        #set scale_after
        scale_after = "Celsius"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet Kelvin to proper Celsius
        result = num_convet-273.15
    #Celsius -> Kelvin mode
    elif num_sub == 4:
        print("\nCelsius -> Kelvin!\n")
        #set scale_before
        scale_before = "Celsius"
        #set scale_after
        scale_after = "Kelvin"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet Celsius to proper Kelvin
        result = num_convet+273.15
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
    #Check the sub-menu number is valid and get the string->number
    num_sub = check_valid_num(num_sub, 1, 3)

    #Byte -> Byte mode
    if num_sub == 1:
        print("\nByte -> Bit!\n")
        #set scale_before
        scale_before = "Byte"
        #set scale_after
        scale_after = "Bit"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet Byte to proper Bit
        result = num_convet*8
    #MegaByte -> Byte mode
    elif num_sub == 2:
        print("\nMegaByte -> Byte!\n")
        #set scale_before
        scale_before = "MegaByte"
        #set scale_after
        scale_after = "Byte"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet MegaByte to proper Byte
        result = num_convet*1000000
    #GigaByte -> MegaByte mode
    elif num_sub == 3:
        print("\nGigaByte -> MegaByte!\n")
        #set scale_before
        scale_before = "GigaByte"
        #set scale_after
        scale_after = "MegaByte"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet GigaByte to proper MegaByte
        result = num_convet*1000
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
    #Check the sub-menu number is valid and get the string->number
    num_sub = check_valid_num(num_sub, 1, 3)

    #Year -> Month mode
    if num_sub == 1:
        print("\nYear -> Month!\n")
        #set scale_before
        scale_before = "Year"
        #set scale_after
        scale_after = "Month"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet Year to proper Month
        result = num_convet*12
    #Year -> Week mode
    elif num_sub == 2:
        print("\nYear -> Week!\n")
        #set scale_before
        scale_before = "Year"
        #set scale_after
        scale_after = "Week"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet Year to proper Week
        result = num_convet*52.143
    #Year -> Day mode
    elif num_sub == 3:
        print("\nYear -> Day!\n")
        #set scale_before
        scale_before = "Year"
        #set scale_after
        scale_after = "Day"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet Year to proper Day
        result = num_convet*365

#print result
print("\nResult :", num_convert, scale_before, "-> ", '%.2f' % result, scale_after)
