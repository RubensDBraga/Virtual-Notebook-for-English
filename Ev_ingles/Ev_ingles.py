from Create import *
from Header import *
from time import sleep

file = 'Evolution_in_English.txt'
headerfile('Evolution in English')
sleep(1)
createfile(file)
sleep(1)
while True:
    try:
        option = menu(["See what you've already learned",
                       "Register new Learning", "Exit. Bye bye"])
    except (ValueError):
        print('Option not found. Please choose again')
        sleep(0.5)
    else:
        if option == 1:
            read(file)
            continue
        if option == 2:
            print('\nWhat do we have for today?')
            english = str(input('Your new learning in English: '))
            portuguese = str(input('Now, in Portuguese: '))
            create(english, portuguese)
            continue
        if option == 3:
            sleep(0.5)
            print('\nBye! Happy studying, see you next time!\n')
            break
        else:
            print('Option not found. Please choose again')
            sleep(0.5)
