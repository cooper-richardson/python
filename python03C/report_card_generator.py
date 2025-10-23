name = input("Student's name: ")
subject1 = str(input("Subject 1: "))
grade1 = int(input("Grade 1 (out of 100): "))
subject2 = str(input("Subject 2: "))
grade2 = int(input("Grade 2 (out of 100): "))
subject3 = str(input("Subject 3: "))
grade3 = int(input("Grade 3 (out of 100): "))
subject4 = str(input("Subject 4: "))
grade4 = int(input("Grade 4 (out of 100): "))
subject5 = str(input("Subject 5: "))
grade5 = int(input("Grade 5 (out of 100): "))

print("REPORT CARD")
print(f"Student: {name}")

print(f"{subject1} grade is {grade1}")
print(f"{subject2} grade is {grade2}")
print(f"{subject3} grade is {grade3}")
print(f"{subject4} grade is {grade4}")
print(f"{subject5} grade is {grade5}")

all = grade1 + grade2 + grade3 + grade4 + grade5
avg = all / 5

print(f"Average grade: {avg}")
if avg > 89:
    print("Letter grade: A")
elif avg > 79:
    print("Letter grade: B")
elif avg > 69:
    print("Letter grade: C")
elif avg > 59:
    print("Letter grade: D")
else:
    print("Letter grade: F")