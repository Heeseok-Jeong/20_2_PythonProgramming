#스토리 : 맥도날드 주문
#캐릭터 : 1. Big boy, 2. Healthy girl, 3. Old man
#이벤트 : 1. 햄버거, 2.감자튀김, 3. 콜라, 4.아이스크림
#점수(6보다 커야함 )
#1. (2, 1), (1, 2), (2, 1)
#2. (2, 1), (2, 1), (2, 1)
#3. (2, 1), (1, 2), (1, 2)
#4. (2, 1), (2, 1), (2, 1)

print("Welcome to 'Order in MxxDonalds' Game!") # Q1

characterList = ['1. Tom', '2. Sally', '3. Mark'] # Q2-A set 3 names
is_input_ok = False # Q2-B
while(not is_input_ok): # Q2-B
    print("\nChoose your character", characterList, ": ", end = '') # Q2-B
    characterNum = input() # Q2-B
    if not characterNum.isdecimal(): # Q2-B
        print('Non numeric input. Please choose in range 1~3.') # Q2-B
        continue # Q2-B
    characterNum = int(characterNum) # Q2-B
    if not (1 <= characterNum <= 3): # Q2-B
        print('Out of range. Please choose in range 1~3.') # Q2-B
        continue # Q2-B
    is_input_ok = True # Q2-B
print("=> Your character is", characterList[characterNum-1][3:], ".") # Q2-C

print("\nLet's order in MxxDonalds!") # Q3

eventList = ['Hamburger', 'French fries', 'Cola', 'Icecream'] # Q4-A
optionList = [['1. O', '2. X'], ['1. Yes', '2. No'], ['1. Y', '2. N'], ['1. Buy', '2. Don\'t buy']] # Q4-B
score = 0 # set score

for eventNum in range(4): # Q4
    is_input_ok = False # Q4-B-2
    while(not is_input_ok): # Q4-B-2
        print("\nEvent", eventNum+1, ": Buying", eventList[eventNum], ", what is your choice?") # Q4-A
        print(optionList[eventNum], ": ", end = '') # Q4-B-1
        optionNum = input() # Q4-B-2
        if not optionNum.isdecimal(): # Q4-B-2
            print('Non numeric input. Please choose in range 1~2.') # Q4-B-2
            continue # Q4-B-2
        optionNum = int(optionNum) # Q4-B-2
        if not (1 <= optionNum <= 2): # Q4-B-2
            print('Out of range. Please choose in range 1~2.') # Q4-B-2
            continue # Q4-B-2
        is_input_ok = True # Q4-B-2

    if eventNum == 0: # Q4-C
        if characterNum == 2: # Q4-C
            if optionNum == 1: # Q4-C
                score += 1 # Q4-C
            else: # Q4-C
                score += 2 # Q4-C
        else: # Q4-C
            if optionNum == 1: # Q4-C
                score += 2 # Q4-C
            else: # Q4-C
                score += 1 # Q4-C
    elif eventNum == 1: # Q4-C
        if optionNum == 1: # Q4-C
            score += 2 # Q4-C
        else: # Q4-C
            score += 1 # Q4-C
    elif eventNum == 2: # Q4-C
        if characterNum == 3: # Q4-C
            if optionNum == 1: # Q4-C
                score += 1 # Q4-C
            else: # Q4-C
                score += 2 # Q4-C
        else: # Q4-C
            if optionNum == 1: # Q4-C
                score += 2 # Q4-C
            else: # Q4-C
                score += 1 # Q4-C
    else: # Q4-C
        if characterNum == 1: # Q4-C
            if optionNum == 1: # Q4-C
                score += 1 # Q4-C
            else: # Q4-C
                score += 2 # Q4-C
        else: # Q4-C
            if optionNum == 1: # Q4-C
                score += 2 # Q4-C
            else: # Q4-C
                score += 1 # Q4-C
    print("=>", characterList[characterNum-1][3:], ",", eventList[eventNum], ",", optionList[eventNum][optionNum-1][3:], ", Your current score :", score) # Q4-D

    if score < eventNum*2: # Q4-E
        print("(warning : Your character doesn't like those decisions!)") # Q4-E

print("\n\n==>Your final score :", score) # Q5
if score >= 6: # Q5
    print("\tMission Completed!") # Q5
else: # Q5
    print("\tMission Failed!") # Q5
input() # Q5
