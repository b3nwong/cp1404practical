"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
grade = ""

def get_score():
    global score
    score = float(input("Enter score: "))


def check_grade():
    global grade
    if 0 <= score <= 100:
        if score >= 90:
            grade = "Excellent"
        elif score >= 50:
            grade = "Passable"
        elif score < 50:
            grade = "Bad"
    else:
        grade = "Invalid score"

def main():
    get_score()
    check_grade()
    return grade
print(main())
