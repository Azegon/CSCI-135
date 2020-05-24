fort_list = ['Fortune 1', 'Fortune 2', 'Fortune 3', 'Fortune 4']


user_resp = "Y"
while 1 == 1:
    user_num1 = int(input('Enter a Number Between 1 and 4: '))
    if user_resp == 'Y':
        if user_num1 == 1:
            # num 7 or 8
            user_num2 = int(input('Pick 7 or 8: '))
            if user_num2 == 7:
                print(fort_list[1])
            elif user_num2 == 8:
                print(fort_list[2])
            else:
                print('Invalid Number')
        elif user_num1 == 2:
            # num 3 or 4
            user_num2 = int(input('Pick 3 or 4: '))
            if user_num2 == 3:
                print(fort_list[3])
            elif user_num2 == 4:
                print(fort_list[0])
            else:
                print('Invalid Number')
        elif user_num1 == 3:
            # num 5 or 6
            user_num2 = int(input('Pick 5 or 6: '))
            if user_num2 == 5:
                print(fort_list[0])
            elif user_num2 == 6:
                print(fort_list[1])
            else:
                print('Invalid Number')
        elif user_num1 == 4:
            # num 1 or 2
            user_num2 = int(input('Pick 1 or 2: '))
            if user_num2 == 1:
                print(fort_list[2])
            elif user_num2 == 2:
                print(fort_list[3])
            else:
                print('Invalid Number')
        else:
            print('Invalid Number')
        user_resp = input('Restart Y or N: ')
    elif user_resp == 'N':
        break
    else:
        print('Invalid Response')
        user_resp = input('Restart Y or N: ')
