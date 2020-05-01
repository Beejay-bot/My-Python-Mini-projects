'''
    This is a multy line
    code.
    This is  comment
'''


import re

print("Magical calculator")
print("Type quit to exit\n")

previous = 0 
run = True


def performMath():
    global run 
    global previous
    equation= ""


    #if there has been a previous calculation, use that result as the  prompt
    if previous == 0:
        equation = input("ENTER EQUATION : ")
    else:
        equation =  input(str(previous))

        
    #if user quit -->
    if equation == 'quit':
        print("Goodbye Human")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous ==0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

            print(previous)

while run:
    performMath()