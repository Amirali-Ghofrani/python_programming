
grade = int(input("grade: "))                 # gets the grade from the user
score = 0

# prints the score and a comment for the user based on the grade entered:

if grade >= 80:
    score = score + 10
    print("Wonderful: A+\n", "score: ", score, sep = "")   

elif 50 <= grade < 80:
    score = score + 5
    print("passed! well done!\n", "score: ", score, sep = "")
    

elif grade < 50:
    print("more effort makes the results better!\n", "score: ", score, sep = "")
    
    

# another form:
height = 180
 
stature = "tall" if height >= 180 else "not tall" 
print("\n", stature, sep="")

    