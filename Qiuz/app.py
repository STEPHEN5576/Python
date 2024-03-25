print("Welcome to my Computer Quiz!")

playing = input("Do you want to Play? ")

if(playing.lower()) != "yes":
    quit()

print("Okay! let's play :)")
score =0
answer = input("what deos cpu stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incoorect!')

answer = input("what deos gpu stand for? ")
if answer.lower() == "grapics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incoorect!')

answer = input("what deos RAM stand for? ")
if answer.lower() == "Random acess memory":
    print('Correct!')
    score += 1
else:
    print('Incoorect!')

answer = input("what deos PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print('Incoorect!')
print('your score is' + str(score))
print("you got "+ str((score/4)*100) + "%.")
