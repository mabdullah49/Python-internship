
def get_letter_grade(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 85:
        return "A-"
    elif score >= 80:
        return "B+"
    elif score >= 75:
        return "B"
    elif score >= 70:
        return "B-"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    elif score >= 0:
        return "F"
    else:
        return None  

def print_grade_summary(student_name, score):
    grade = get_letter_grade(score)
    if grade is not None:
        print(f"Student {student_name} scored {score} → Grade: {grade}")
    else:
        print("Invalid score entered. Please enter a value between 0 and 100.")


try:
    name = input("Enter student name: ")
    score_input = input("Enter score (0–100): ")
    score = float(score_input)

    if 0 <= score <= 100:
        print_grade_summary(student_name=name, score=score)
    else:
        print("Error: Score must be between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a numeric score.")
