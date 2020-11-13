from datetime import date, datetime

def check_valid_format(option, date_str):
    result = True
    if option == 1:
        print(date.fromisoformat(date_str))
    else:
        pass

    return result

def check_valid_date():
    pass

def get_weekday():
    pass

print("Welcome to Date Program :)\n")
print("Option 1 : YYYY-MM-DD")
print("Option 2 : MM/DD/YYYY\n")

option = 0
while not (1 <= option <= 2):
    option = int(input("Choose an option (1 or 2) : "))
print()

is_date_match_with_option = False
while not is_date_match_with_option:
    date_str = input("Input a valid date : ")
    if check_valid_format(option, date_str):
        if check_valid_date(date_str):
            weekday = get_weekday(date_str)
            print("Weekday :", weekday)

            year_after_date = date_str
            if option == 1:
                year = date_str[0:4]
                year += 1
                year_after_date[0:4] = year
            elif option == 2:
                year = date_str[:-4]
                year += 1
                year_after_date[:-4] = year
            print(year_after_date)
            year_after_weekday = get_weekday(year_after_date)
