print("Welcome to my Movie quiz\n")

playing = input("Shall we play a game? ")
print(playing)

if playing != "yes":
    quit()

print("Now. Shall we begin")
score =0

# Question 1
answer = input("Is Batman a Marvel or DC movie? ")

if answer == "DC":
    print("Correct")
    score+=1
else: 
    print("Wrong")

# Question 2
answer = input("Is Captain Kirk in Star Wars or Star Trek? ")

if answer == "Star Trek":
    print("Correct")
    score+=1
else: 
    print("Wrong")

# Question 3
answer = input("What Sci-Fi has a killer Time travel Robot? ")

if answer == "Terminator":
    print("Correct")
    score+=1
else: 
    print("Wrong")

# Question 4
answer = input("Which famous spy drink is a Vodka Martini stirred not shaken? ")

if answer == "James Bond":
    print("Correct")
    score+=1
else: 
    print("Wrong")

# Question 5
answer = input("Which movie has the motto 'Manners Maketh Man'? ")

if answer == "Kingsman":
    print("Correct")
    score+=1
else: 
    print("Wrong")

#print score
print("You answered " + str(score) + " questions correct")

#print score %
print("You answered " + str((score / 5) * 100) + "%")

