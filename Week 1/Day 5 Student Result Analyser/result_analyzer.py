import csv

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


marks_list = []
students = []

print("=== STUDENT RESULT ANALYTICS SYSTEM ===\n")

with open("marks.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Name\tMarks\tGrade")
    print("-------------------------")

    for row in reader:
        name = row["Name"]
        marks = float(row["Marks"])
        grade = get_grade(marks)

        students.append((name, marks))
        marks_list.append(marks)

        print(f"{name}\t{marks}\t{grade}")

# Summary Calculations
average = sum(marks_list) / len(marks_list)
highest = max(marks_list)
lowest = min(marks_list)

passed = len([m for m in marks_list if m >= 40])
failed = len(marks_list) - passed
pass_percentage = (passed / len(marks_list)) * 100

# Topper
topper = max(students, key=lambda x: x[1])

print("\n--- CLASS PERFORMANCE SUMMARY ---")
print(f"Average Marks: {average:.2f}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")
print(f"Students Passed: {passed}")
print(f"Students Failed: {failed}")
print(f"Pass Percentage: {pass_percentage:.2f}%")
print(f"Topper: {topper[0]} with {topper[1]} marks")
