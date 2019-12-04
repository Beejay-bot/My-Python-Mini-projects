# player_name = input('what is your name? : ')
# print(player_name)
# import random
# while True:
#     rolled_num = random.randint(1,6)
#     print(rolled_num)
#     if rolled_num is 6:
#         print (player_name + str("The dice rolled and you got: ") + rolled_num + str("You Won!!!!"))
#     if rolled_num >6:
#         print(player_name + "The dice rolled and you got:" + rolled_num + 'sorry you lost try again')
#     input("Press any key to roll again.")    


# player_name = input('what is your name? :')
# print(player_name)
# import random
# for i in range (5):
#     die_1 = random.randint(1,6)
#     die_2 = random.randint (1,6)
#     print('die 1 is', die_1, 'die 2 is', die_2)
#     if die_1 == die_2 and die_1 == 6:
#         print(player_name + ' yeah!!!, you won')
#         break
#     else:
#         print('oops ' + player_name +  ', you lost')
# input('press enter to play again')

                                            # MULTIPLICATION TABLE ASSIGNMENT
# num = int(input("Enter the number: "))
# print("Multiplication Table of", num)
# for i in range(1, 14):
#    print(num,"X",i,"=",num * i)


                    # COUNTDOWN TIMER ALARM
# import time
# def countdown(t):
#         while t:
#             mins, secs = divmod(t, 60)
#             timer = '{:02d}:{:02d}'.format(mins, secs)
#             print(timer, end="\r")
#             time.sleep(1)
#             t -= 1
#         print('Its time!!!')
# t = input("Enter the time in seconds: ") 
# countdown(int(t))

import time
boom = int(input("Countdown from:"))
while boom > 0:
    time.sleep(1)
    print(boom, "\r",  end="")
    boom -= 1
print("BLASTOFF!")

# for i in range (1,13):
#     for n in range (1,12):
#         print(f"{n} x {i} = {n * 1}".center(12), end="")
#     print("\n")
