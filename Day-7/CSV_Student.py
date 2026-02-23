import csv
import os

file_exists = os.path.isfile("students.csv")
file_empty = os.path.getsize("students.csv") == 0 if file_exists else True

n = int(input("Enter number of students: "))

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists or file_empty:
        writer.writerow(["Name", "Grade", "Status"])

    for i in range(n):
        print(f"\nEnter details for student {i + 1}")
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        status = input("Enter status (Pass/Fail): ")

        writer.writerow([name, grade, status])

print("\nStudent data saved.\n")

print("Students who Passed:")

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  

    for row in reader:
        if row[2].strip().lower() == "pass":
            print(row[0])
