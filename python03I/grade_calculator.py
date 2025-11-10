def display_menu():
    """Display the main menu options."""
    # YOUR CODE HERE
    while True:
        print("Grade Calculator")
        print("Enter 1 to add a grade")
        print("Enter 2 to view grade statistics")
        print("Enter 3 to exit")
        start = int(input(""))
        if start == 1:
            add_grade()
        elif start == 2:
            display_report()
        elif start == 3:
            break
avg = 0
        

def add_grade():
    """
    Prompt for a new grade and add it to the list.
    Return the updated list.
    """
    # YOUR CODE HERE
    new_grade = float(input("Enter new grade: "))
    student_grades.append(new_grade)
    pass

def calculate_average():
    """Calculate and return the average of grades."""
    # Hint: Watch for empty list!
    # YOUR CODE HERE
    if student_grades == []:
        print("Error; No grades entered")
    else:
        tSum = sum(student_grades)
        quantity = len(student_grades)
        avg = tSum / quantity
        print(f"Grade Average: {avg}")
        return avg
    pass

def get_letter_grade(avg):
    """Convert numeric average to letter grade. Return the letter."""
    # YOUR CODE HERE
    letter_grade = "TBD"
    if avg >= 89:
        letter_grade = "A"
    elif avg >= 79:
        letter_grade = "B"
    elif avg >= 69:
        letter_grade = "C"
    elif avg >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    print(letter_grade)
    pass

def find_highest():
    """Find and return the highest grade."""
    # YOUR CODE HERE
    highest = max(student_grades)
    print(highest)
    pass

def find_lowest():
    """Find and return the lowest grade."""
    # YOUR CODE HERE
    lowest = min(student_grades)
    print(lowest)
    pass

def display_report():
    """Display complete grade report with statistics."""
    # YOUR CODE HERE
    # Should show: all grades, average, letter grade, highest, lowest
    print(f"All Grades: {student_grades}")
    calculate_average()
    get_letter_grade(avg)
    find_highest()
    find_lowest()
    pass

# Main program
print("=== STUDENT GRADE CALCULATOR ===")
student_grades = []

# YOUR CODE HERE - Write the main program loop
# Allow user to add student_grades, view report, and quit

display_menu()