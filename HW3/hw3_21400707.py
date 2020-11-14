from datetime import date, datetime
import random

def get_date_format():
    date_format = ''
    while not (date_format == '1' or date_format == '2'):
        date_format = input("Choose a Date Format (1 or 2) : ")
    date_format = int(date_format)
    print()
    return date_format

def check_valid_format(date_str, date_format):
    result = True
    len_date_str = len(date_str)
    if date_format == 1:
        if len_date_str == 10:
            for i in range(len_date_str):
                if i < 4:
                    if not date_str[i].isdecimal():
                        result = False
                        break
                elif i == 4 or i == 7:
                    if not date_str[i] == '-':
                        result = False
                        break
                elif i < 7:
                    if not date_str[i].isdecimal():
                        result = False
                        break
                elif i < len_date_str:
                    if not date_str[i].isdecimal():
                        result = False
                        break
        else:
            result = False
    else:
        if len_date_str == 10:
            for i in range(len_date_str):
                if i < 2:
                    if not date_str[i].isdecimal():
                        result = False
                        break
                elif i == 2 or i == 5:
                    if not date_str[i] == '/':
                        result = False
                        break
                elif i < 5:
                    if not date_str[i].isdecimal():
                        result = False
                        break
                elif i < len_date_str:
                    if not date_str[i].isdecimal():
                        result = False
                        break
        else:
            result = False
    if result:
        return True
    else:
        print("Error : Invalid Date Format!")
        return False

def check_valid_date(date_str, date_format):
    if date_format == 1:
        month = int(date_str[5:7])
        day = int(date_str[-2:])
    else:
        month = int(date_str[:2])
        day = int(date_str[3:5])

    if not (1 <= month <= 12):
        print("Month is invalid.")
        return False

    if month%2 == 1 and not (1 <= day <= 31):
        print("Day is invalid.")
        return False
    elif month == 2 and not (1 <= day <= 28):
        print("Month is invalid.")
        return False
    elif month%2 == 0 and not (1 <= day <= 30):
        print("Day is invalid.")
        return False

    return True

def get_weekday(date_str):
    dayString = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if '-' in date_str:
        year = int(date_str[0:4])
        month = int(date_str[5:7])
        day = int(date_str[-2:])
    elif '/' in date_str:
        year = int(date_str[-4:])
        month = int(date_str[:2])
        day = int(date_str[3:5])
    _datetime = datetime(year, month, day)
    return dayString[_datetime.weekday()]

def compose_random_date():
    date_format = random.randrange(1, 3)
    year = str(random.randrange(2000, 2021))
    month = random.randrange(1, 20)
    if month < 10:
        month = '0' + str(month)
    day = random.randrange(1, 50)
    if day < 10:
        day = '0' + str(day)

    if date_format == 1:
        return year+'-'+str(month)+'-'+str(day)
    else:
        return str(month)+'/'+str(day)+'/'+year


print("Welcome to Date Program :)\n")
print("Date Format Option 1 : YYYY-MM-DD")
print("Date Format Option 2 : MM/DD/YYYY\n")

date_format = get_date_format()

while True:
    date_str = input("Input a valid date : ")
    if check_valid_format(date_str, date_format):
        if check_valid_date(date_str, date_format):
            weekday = get_weekday(date_str)
            print()
            print("Weekday :", weekday)
            year_after_date = ''
            if date_format == 1:
                year = int(date_str[0:4])
                year += 1
                year_digits = 0
                temp_year = year
                while temp_year >= 1:
                    temp_year /= 10
                    year_digits += 1
                new_year = ''
                max_digits = 4
                if temp_year == 10000:
                    max_digits = 5
                for _ in range(max_digits-year_digits):
                    new_year += '0'
                new_year += str(year)
                month = date_str[5:7]
                day = date_str[-2:]
                year_after_date = new_year+'-'+month+'-'+day
            else:
                year = int(date_str[6:])
                year += 1
                year_digits = 0
                temp_year = year
                while temp_year >= 1:
                    temp_year /= 10
                    year_digits += 1
                new_year = ''
                max_digits = 4
                if temp_year == 10000:
                    max_digits = 5
                for _ in range(max_digits-year_digits):
                    new_year += '0'
                new_year += str(year)
                month = date_str[:2]
                day = date_str[3:5]
                year_after_date = month+'/'+day+'/'+new_year
            year_after_weekday = get_weekday(year_after_date)

            print("One year after date :", year_after_date, ", its weekday :", year_after_weekday)
            print()


            print("Do you want to search another date?")
            again = input("Then please enter 'y', otherwise, the program will proceed random auto-test : ")
            print()
            if again == 'y':
                date_format = get_date_format()
                continue
            else:
                print("The random auto-testing is starting....\n")
                for _ in range(10):
                    date_format = random.randrange(1, 3)
                    date_str = compose_random_date()
                    if date_format == 1:
                        print("The date to test :", date_str, ": with the format : YYYY-MM-DD")
                    else:
                        print("The date to test :", date_str, ": with the format : MM/DD/YYYY")
                    if check_valid_format(date_str, date_format):
                        if check_valid_date(date_str, date_format):
                            weekday = get_weekday(date_str)
                            print("Weekday :", weekday)
                    print()
                break
