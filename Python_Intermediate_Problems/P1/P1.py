import random
from random import randrange
from datetime import timedelta
from datetime import datetime
import json

stud_count = int(input("Enter the number of students to generate: "))
exam_date = int(input("Enter  examination year: "))
stud_names = [
    "phoneix",
    "sage",
    "jett",
    "breach",
    "reyna",
    "yoru",
    "sova",
    "clove",
    "omen",
    "viper",
    "raze",
    "fade",
]
subjects = ["Python", "Database", "Computer Networks"]

department = ["Computer Science", "Information Technology", "Electronics", "Mechanical"]
start_range = datetime(exam_date, 1, 1, 0, 0)
end_range = datetime(exam_date + 1, 1, 1, 0, 0)
data = []


def random_date(start_date, end_date):
    end_date = end_date.date()
    start_date = start_date.date()
    delta = end_date - start_date
    random_days = random.randrange(delta.days + 1)
    return start_date + timedelta(days=random_days)


for i in range(0, stud_count):
    students = {}
    subject_marks = {}
    fail_count = 0
    avg_list = []
    pass_count = 0
    id = random.randint(1, 10000)
    name = random.choice(stud_names)
    dept = random.choice(department)
    age = random.randint(18, 25)
    for s in subjects:
        subject_marks[s] = random.randrange(0, 100)
    total_marks = (
        int(subject_marks["Python"])
        + int(subject_marks["Database"])
        + int(subject_marks["Computer Networks"])
    )
    avg_marks = total_marks / 3
    if any(mark < 40 for mark in subject_marks.values()):
        result = "Fail"
        fail_count += 1
    else:
        result = "Pass"
        pass_count += 1
    random_d = random_date(start_range, end_range)
    random_d = random_d.strftime("%Y-%m-%d")
    students["StudentID"] = id
    students["name"] = name
    students["age"] = age
    students["department"] = dept
    students["marks"] = subject_marks
    students["total"] = total_marks
    students["average"] = avg_marks
    avg_list = avg_list.append(avg_marks)
    students["result"] = result
    students["exam-date"] = random_d
    data.append(students)
with open("students.json", "w") as file:
    json.dump(data, file, indent=4)
for avg in avg_list:
    print(avg)

print("Student data successfully written to students.json")
