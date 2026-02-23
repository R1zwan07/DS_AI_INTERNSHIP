import pandas as pd

grades = pd.Series([85, None, 92, 45, None, 78, 55])

missing_values = grades.isnull()

filled_grades = grades.fillna(0)

passed_students = filled_grades[filled_grades > 60]

print("Original Grades Series:\n")
print(grades)

print("\nMissing Values (True = Missing):\n")
print(missing_values)

print("\nGrades After Filling Missing Values:\n")
print(filled_grades)

print("\nScores Greater Than 60:\n")
print(passed_students)
