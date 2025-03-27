import random

def create_phone_number():
    randnumber = 'x'
    #your code here
    number = '(xxx) xxx-xxxx'
    loop1 = True
    while loop1 == True:
        number = number.replace('x', randnumber, 1)
        number = str(number)
        if 'x' in number:
            randnumber = random.randint(0,9)
            randnumber = str(randnumber)
            loop1 = True
        
        else:
            print(f'Your phone number is: {number}')
            loop1 = False


create_phone_number()