#YOU ARE BUILDING A SMALL PROGRAM FOR A SCHOOL.THE USER MUST ENTER THE STUDENTS NAME AND MARKS IN THREE SUBJECTS. THE PROGRAM SHOULD CALCULTE THE TOTAL,AVERAGE AND DISPLAY A GRADE.IF MARK ARE NOT BETWEEN 0 AND 100, SHOW AN ERRROR MESSAGE
name = input("Enter student name: ")


marks1 = int(input("Enter marks for Subject 1: "))
marks2 = int(input("Enter marks for Subject 2: "))
marks3 = int(input("Enter marks for Subject 3: "))



total = marks1 + marks2 + marks3
average = total / 3

    
if average >= 90 and average<=100:
    grade = "A"
elif 90 > average >= 75 :
    grade = "B"
elif 75 > average >= 60:
    grade = "C"
elif 60 > average >= 40:
    grade = "D"
elif average < 40:
    grade = "F"
else:
    print("ENTER VALUE BELOW 100")

    # Output
print("\n--- STUDENT RESULT ---")
print("Name:", name)
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
