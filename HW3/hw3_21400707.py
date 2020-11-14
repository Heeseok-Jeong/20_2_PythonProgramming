from datetime import datetime #Q3
import random #Q10, Q11

def get_date_format(): #Q4
    date_format = '' #Q4
    while not (date_format == '1' or date_format == '2'): #Q4
        date_format = input("Choose a Date Format (1 or 2) : ") #Q4
    date_format = int(date_format) #Q4
    print() #Q4
    return date_format #Q4

def check_valid_format(date_str, date_format): #Q1
    result = True #Q1
    len_date_str = len(date_str) #Q1
    if date_format == 1: #Q1
        if len_date_str == 10: #Q1
            for i in range(len_date_str): #Q1
                if i < 4: #Q1-D
                    if not date_str[i].isdecimal(): #Q1-D
                        result = False #Q1-D
                        break #Q1-D
                elif i == 4 or i == 7: #Q1-D
                    if not date_str[i] == '-': #Q1-D
                        result = False #Q1-D
                        break #Q1-D
                elif i < 7: #Q1-D
                    if not date_str[i].isdecimal(): #Q1-D
                        result = False #Q1-D
                        break #Q1-D
                elif i < len_date_str: #Q1-D
                    if not date_str[i].isdecimal(): #Q1-D
                        result = False #Q1-D
                        break #Q1-D
        else: #Q1-D
            result = False #Q1-D
    else: #Q1
        if len_date_str == 10: #Q1
            for i in range(len_date_str): #Q1
                if i < 2: #Q1-D
                    if not date_str[i].isdecimal(): #Q1-D
                        result = False #Q1-D
                        break #Q1-D
                elif i == 2 or i == 5: #Q1-D
                    if not date_str[i] == '/': #Q1-D
                        result = False #Q1-D
                        break #Q1-D
                elif i < 5: #Q1-D
                    if not date_str[i].isdecimal(): #Q1-D
                        result = False #Q1-D
                        break #Q1-D
                elif i < len_date_str: #Q1-D
                    if not date_str[i].isdecimal(): #Q1-D
                        result = False #Q1-D
                        break #Q1-D
        else: #Q1-D
            result = False #Q1-D
    if result: #Q1-A
        return True #Q1-A
    else: #Q1-D
        print("Date format is invalid.") #Q1-D
        return False #Q1-D

def check_valid_date(date_str, date_format): #Q2
    if date_format == 1: #Q2
        month = int(date_str[5:7]) #Q2-C
        day = int(date_str[-2:]) #Q2-C
    else: #Q2
        month = int(date_str[:2]) #Q2-C
        day = int(date_str[3:5]) #Q2-C

    if not (1 <= month <= 12): #Q2-A
        print("Month is invalid.") #Q2-D
        return False #Q2-D

    if month%2 == 1 and not (1 <= day <= 31): #Q2-D
        print("Day is invalid.") #Q2-D
        return False #Q2-D
    elif month == 2 and not (1 <= day <= 28): #Q2-D
        print("Month is invalid.") #Q2-D
        return False #Q2-D
    elif month%2 == 0 and not (1 <= day <= 30): #Q2-D
        print("Day is invalid.") #Q2-D
        return False #Q2-D

    return True #Q2-D

def get_weekday(date_str): #Q3
    dayString = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] #Q3
    if '-' in date_str: #Q3
        year = int(date_str[0:4]) #Q3
        month = int(date_str[5:7]) #Q3
        day = int(date_str[-2:]) #Q3
    elif '/' in date_str: #Q3
        year = int(date_str[-4:]) #Q3
        month = int(date_str[:2]) #Q3
        day = int(date_str[3:5]) #Q3
    _datetime = datetime(year, month, day) #Q3
    return dayString[_datetime.weekday()] #Q3

def compose_random_date(): #Q10
    date_format = random.randrange(1, 3) #Q10-B
    year = str(random.randrange(2000, 2021)) #Q10-A
    month = random.randrange(1, 20) #Q10-A
    if month < 10: #Q10-B
        month = '0' + str(month) #Q10-B
    day = random.randrange(1, 50) #Q10-A
    if day < 10: #Q10-B
        day = '0' + str(day) #Q10-B

    if date_format == 1: #Q10-B
        return year+'-'+str(month)+'-'+str(day) #Q10-B
    else: #Q10-B
        return str(month)+'/'+str(day)+'/'+year #Q10-B


print("Welcome to Date Program :)\n") #Q4
print("Date Format Option 1 : YYYY-MM-DD") #Q4
print("Date Format Option 2 : MM/DD/YYYY\n") #Q4

date_format = get_date_format() #Q4

while True: #Q5~Q11
    date_str = input("Input a valid date : ") #Q5
    if check_valid_format(date_str, date_format): #Q5-A
        if check_valid_date(date_str, date_format): #Q5-B
            weekday = get_weekday(date_str) #Q6
            print() #Q6
            print("Weekday :", weekday) #Q6
            year_after_date = '' #Q7
            if date_format == 1: #Q7
                year = int(date_str[0:4]) #Q7
                year += 1 #Q7
                year_digits = 0 #Q7
                temp_year = year #Q7
                while temp_year >= 1: #Q7
                    temp_year /= 10 #Q7
                    year_digits += 1 #Q7
                new_year = '' #Q7
                for _ in range(4-year_digits): #Q7
                    new_year += '0' #Q7
                new_year += str(year) #Q7
                month = date_str[5:7] #Q7
                day = date_str[-2:] #Q7
                year_after_date = new_year+'-'+month+'-'+day #Q7
            else: #Q7
                year = int(date_str[6:]) #Q7
                year += 1 #Q7
                year_digits = 0 #Q7
                temp_year = year #Q7
                while temp_year >= 1: #Q7
                    temp_year /= 10 #Q7
                    year_digits += 1 #Q7
                new_year = '' #Q7
                for _ in range(4-year_digits): #Q7
                    new_year += '0' #Q7
                new_year += str(year) #Q7
                month = date_str[:2] #Q7
                day = date_str[3:5] #Q7
                year_after_date = month+'/'+day+'/'+new_year #Q7
            year_after_weekday = get_weekday(year_after_date) #Q7

            print("One year after date :", year_after_date, ", its weekday :", year_after_weekday) #Q7
            print() #Q7

            print("Do you want to search another date?") #Q8
            again = input("Then please enter 'y', otherwise, the program will proceed random auto-test : ") #Q8
            print() #Q8
            if again == 'y': #Q8
                date_format = get_date_format() #Q8
                continue #Q8
            else: #Q9
                print("The random auto-testing is starting....\n") #Q9
                for _ in range(10): #Q11
                    date_format = random.randrange(1, 3) #Q11-A
                    date_str = compose_random_date() #Q10
                    if date_format == 1: #Q11-B
                        print("The date to test :", date_str, ": with the format : YYYY-MM-DD") #Q11-B
                    else: #Q11-B
                        print("The date to test :", date_str, ": with the format : MM/DD/YYYY") #Q11-B
                    if check_valid_format(date_str, date_format): #Q11-C
                        print("Format check clear") #Q11-C
                        if check_valid_date(date_str, date_format): #Q11-D
                            print("Date check clear") #Q11-D
                            weekday = get_weekday(date_str) #Q11-E
                            print("Weekday :", weekday) #Q11-E
                    print() #Q11-E
                break
