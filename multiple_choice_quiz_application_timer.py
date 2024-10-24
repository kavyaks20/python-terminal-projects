print ("QUIZ CONTEST")
print (str(input("enter your name: ")))
print (int(input("enter your register number:")))

score = 0
print("who is the father of nation ?\n \n A: Gandhi \n B:nehru \n C: sardhar \n D: Ambedkar")

q1= str(input)
#start timer
if q1 == 'A':
    print("correct")

    score = score +1

print("what is the national flower of India ?\n \n A: Rose \n B: Lotus \n C: Jasmine \n D: Lilly")
q2 = str(input)
if q2 == 'B':
    print("correct")
    score =score+1
print("What is the national animal of india ? \n A: Lion \n B : Cat \n C: Tiger \n D:Dog")
q3 = str(input)
if q3 == 'C':
    print("correct")

    score = score+1
print("Who is the first president of india? \n A: Rajendra prasad \n B: Subash \n C: Rahul \n D : Rajeev ")
q4 = str(input)
if q4=='A':
    print("correct")

    score = score+1

print ("your total score is :",score)



