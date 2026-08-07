import csv
from grading import get_grade

with open("students.csv", "r") as file, open(
    "students_results.csv", "w", newline=""
) as outfile:
    reader = csv.DictReader(file)
    field_names = reader.fieldnames + ["total", "average", "grade"]
    writer = csv.DictWriter(outfile, fieldnames=field_names)
    writer.writeheader()
    for d in reader:
        d["total"] = int(d["physics"]) + int(d["maths"]) + int(d["chemistry"])
        d["average"] = round(d["total"] / 3, 2)
        d["grade"] = get_grade(d["average"])
        writer.writerow(d)
