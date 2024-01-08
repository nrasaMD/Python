NUM_GRDS = 3
grades=[-1] * NUM_GRDS # variables for 3 grades
grdTotal = int(0)  #variable for the running total
avg = float(0.0)
grdStr = ""

# enter grades and print grade str 100, 90, and 85
for numTest in range(NUM_GRDS):
  grades[numTest] = int(input("Enter grade: ")) 
  print ("  Grade", str(numTest+1) + ":" , format(grades[numTest], "4d"))
  #running total of grades entered
  grdTotal += grades[numTest]

avg = grdTotal / NUM_GRDS 


#format average as a string 
print("  Average:", format(avg,"6.1f"))
