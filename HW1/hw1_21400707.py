#Import sys to use sys.exit()
import sys

##Ask user to quit the program and quit this program
def terminate():
    #explain user to put enter key to quit the program
    print("Please enter to quit the program.")
    #get input to get enter
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

##Check num_convert is valid and return that number
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
        num = int(num)
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

#1. 길이(1. 밀리미터->센티미터, 2. 센티미터->미터, 3. 미터->킬로미터)
#2. 질량(1. 밀리그램->그램, 2. 그램->킬로그램, 3. 킬로그램->톤)
#3. 환율(1. 원->달러, 2. 원->엔, 3. 원->위안)
#4. 주파수(1. 헤르츠->킬로헤르츠, 2. 킬로헤르츠->메가헤르츠, 3.메가헤르츠->기가헤르츠)
#5. 온도(1. 화씨->섭씨, 2. 섭씨->화씨, 3. 켈빈->섭씨, 4. 섭씨->켈빈)
#6. 데이터크기(1. 비트->바이트, 2. 바이트->메가바이트, 3. 메가바이트->기가바이트)
#7. 시간(1. 년->달, 2. 년->주, 3. 년->일)
#Length Converter function
if num_func == 1:
    #Show user what function chose
    print("\nLength Converter!\n")
    #Show user what sub-menu of Length Converter exist
    print("Sub-Menu")
    print("1-1. millimeters -> centimeters")
    print("1-2. centimeters -> meters")
    print("1-3. meters -> kilometers")

    #Get a sub-menu number user want to use
    num_sub = input("Which sub-menu do you want?(1~3) : ")
    #Check the sub-menu number is valid and get the string->number
    num_sub = check_valid_num(num_sub, 1, 3)

    #millimeters -> centimeters
    if num_sub == 1:
        print("\nmillimeters -> centimeters!\n")
        #set scale_before
        scale_before = "millimeters"
        #set scale_after
        scale_after = "centimeters"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet millimeters to proper centimeters
        result = num_convet/10
    #millimeters -> centimeters
    elif num_sub == 1:
        print("\nmillimeters -> centimeters!\n")
        #set scale_before
        scale_before = "millimeters"
        #set scale_after
        scale_after = "centimeters"
        #Get a number to convert
        num_convert = input("Put a number to convert(positive integer) : ")
        #Check the sub-menu number is valid and get the string->number
        num_convet = check_valid_num_convert(num_convert)
        #convert num_convet millimeters to proper centimeters
        result = num_convet/10

#print result
print("\nResult : ", num_convert, scale_before, "-> ", '%.2f' % result, scale_after)
