from datetime import datetime #Q8, Q10
import random #Q9, Q10

is_test_mode = False #Q10

age_group_list = ["0-2 years", "3-10 years", "11-65 years", "> 65 years"] #Q1
msmt_site_list = ["Oral", "Ear", "Rectal", "Acillary"] #Q1
temperature_range_table = {} #Q1
temperature_range_table[age_group_list[0]] = {msmt_site_list[0] : [-1, -1], msmt_site_list[1] : [36.4, 38.0], msmt_site_list[2] : [36.6, 38.0], msmt_site_list[3] : [34.7, 37.3]} #Q1
temperature_range_table[age_group_list[1]] = {msmt_site_list[0] : [35.5, 37.5], msmt_site_list[1] : [36.1, 37.8], msmt_site_list[2] : [36.6, 38.0], msmt_site_list[3] : [35.9, 36.7]} #Q1
temperature_range_table[age_group_list[2]] = {msmt_site_list[0] : [36.4, 37.6], msmt_site_list[1] : [35.9, 37.6], msmt_site_list[2] : [37.0, 38.1], msmt_site_list[3] : [35.2, 36.9]} #Q1
temperature_range_table[age_group_list[3]] = {msmt_site_list[0] : [35.8, 36.9], msmt_site_list[1] : [35.8, 37.5], msmt_site_list[2] : [36.2, 37.3], msmt_site_list[3] : [35.6, 36.3]} #Q1

def get_input_list(): #Q3
    input_ment = "\nEnter three values <Age group, Measurement site, Body temperature>\n" #Q3
    input_ment += "You should enter each value exactly matched below conditions.\n" #Q3
    input_ment += "Age group : " + str(age_group_list) + ",\n" #Q3
    input_ment += "Measurement site : " + str(msmt_site_list) + ",\n" #Q3
    input_ment += "Body temperature : positive real number.\n" #Q3
    input_ment += "Keep in mind there are two commas between values (ex. 0-2 years, Rectal, 36.5)\n" #Q3
    input_ment += "Input : " #Q3
    input_list = input(input_ment).split(', ') #Q3
    return input_list #Q3

def check_valid_input(input_list): #Q4-a
    if len(input_list) != 3: #Q4-b
        print("Please input three values with exact format! (Age group, Measurement site, Body temperature)") #Q4-a
        return False #Q4-e

    if input_list[0] not in age_group_list: #Q4-c
        print("Please input valid age group value in the age group list!") #Q4-c
        return False #Q4-e

    if input_list[1] not in msmt_site_list: #Q4-c
        print("Please input valid measurement site value in the measurement site list!") #Q4-c
        return False #Q4-e

    try: #Q4-d
        body_temp = float(input_list[2]) #Q4-d
    except: #Q4-d
        if not is_test_mode: #Q4-d
            print("Please input real number for body temperature value!") #Q4-d
        return False #Q4-e
    if body_temp < 0: #Q4-d
        if not is_test_mode: #Q4-d
            print("Please input positive real number for body temperature value!") #Q4-d
        return False #Q4-e

    return True #Q4-e

def get_body_status(age_group, msmt_site, body_temp): #Q7-a
    body_status = '' #Q7-b
    for i in range(4): #Q7-b
        for j in range(4): #Q7-b
            if age_group_list[i] == age_group and msmt_site_list[j] == msmt_site: #Q7-b
                if temperature_range_table[age_group][msmt_site][0] == -1: #Q7-b
                    body_status = 'Error' #Q7-b
                elif body_temp < temperature_range_table[age_group][msmt_site][0]: #Q7-b
                    body_status = 'Low' #Q7-b
                elif temperature_range_table[age_group][msmt_site][0] <= body_temp < temperature_range_table[age_group][msmt_site][1]: #Q7-b
                    body_status = 'Normal' #Q7-b
                elif temperature_range_table[age_group][msmt_site][1] <= body_temp: #Q7-b
                    body_status = 'Fever' #Q7-b
                else: #Q7-b
                    print("out") #Q7-b
                    body_status = 'Error' #Q7-b

    return body_status #Q7-c

def make_random_input(): #Q9-a
    age_group = random.choice(age_group_list) #Q9-b
    msmt_site = random.choice(msmt_site_list) #Q9-c
    body_temp = random.uniform(30, 40) #Q9-d
    body_temp = round(body_temp, 2) #Q9-d

    negative_prob = random.randrange(1, 11) #Q9-d
    if 1 <= negative_prob <= 3: #Q9-d
        body_temp *= -1 #Q9-d

    return age_group, msmt_site, body_temp #Q9-e


print("This is Body Temperature program. Welcome :)") #Q2
input_list = get_input_list() #Q3
is_valid_input = check_valid_input(input_list) #Q5

while not is_valid_input: #Q6
    input_list = get_input_list() #Q6
    is_valid_input = check_valid_input(input_list) #Q6

age_group, msmt_site, body_temp = input_list #Q7-a
body_temp = float(body_temp) #Q7-a

body_status = get_body_status(age_group, msmt_site, body_temp) #Q8
if body_status != 'Error': #Q8
    body_status = "The temperature status : " + body_status #Q8
now = datetime.now() #Q8
print(body_status, ", Time :", now) #Q8

print("\nNow the program make and test for 10 random body temperature...\n") #Q10
is_test_mode = True #Q10
test_results = [] #Q10-c
for _ in range(10): #Q10
    result = {} #Q10-a
    random_input_list = list(make_random_input()) #Q10-a
    age_group, msmt_site, body_temp = random_input_list #Q10-a
    body_temp = float(body_temp) #Q10-a
    result["Age group"] = age_group #Q10-a
    result["Measurement site"] = msmt_site #Q10-a
    result["Body temperature"] = body_temp #Q10-a
    body_status = "Error" #Q10-b
    if check_valid_input(random_input_list): #Q10-a
        body_status = get_body_status(age_group, msmt_site, body_temp) #Q10-a
    result["Body status"] = body_status #Q10-a
    now = datetime.now() #Q10-a
    result["Time"] = str(now) #Q10-a
    test_results.append(result) #Q10-c

print("This is the results!") #Q10-c
print(test_results) #Q10-c
