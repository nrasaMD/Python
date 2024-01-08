#Nick Rasa
#Grades

#Initialization
grade = int(0)
message = str("")


#input
grade = int(input("Enter Grade: "))

#Process

if grade >= 90:
    message = "Great job. You made an A!"
elif grade >= 80:
    message = "Good Job. You made a B!"
elif grade >= 70:
    message = "You made a C."
else: message = "You made less than a C. You will have to do better to pass the class."




#output
print ("Grade: ", grade)
print (message)
    
