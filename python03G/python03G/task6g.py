while True:
    grade = int(input("Enter a grade: ")) 
    if grade >= 0 and grade <= 100:
        print(f"Valid, grade accepted: {grade}")
        break
    else:
        print("Invalid must be 0-100")
   