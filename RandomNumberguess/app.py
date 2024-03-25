import random 
top_of_range = input("type a number: ")

if(top_of_range.isdigit):
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('please type a number larger than 0 next time>')
        quit()
else:
    print('please enter digit next time.')
    quit()

random_number = random.randint(0,top_of_range)
if(top_of_range == random_number):
    print('Thats correct')
else:
    print('its wrong answer please try again') 
    print('the number was '+ str(random_number))   

