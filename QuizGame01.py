# percentage out of question 
print("welcome to computer quiz")

playing = input("do you want to play? ")
print(playing)

text ="CHARACTER TO Lower and greater"
print(text.lower())
if playing.lower() !="yes":
    quit()
print("lets play")
score=0
answer=input("what does cpu stands for? ")
if answer.lower() =="central processing unit":
    print("correct")
    score+=1
else:
    print("incorrect")

answer=input("what does gpu stands for? ")
if answer.lower() =="graphics processing unit":
    print("correct")
    score+=1
else:
    print("incorrect")

print(f"you got"+ str(score)+" score for correct question" )