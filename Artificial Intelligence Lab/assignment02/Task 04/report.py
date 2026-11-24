
import csv
import json

student_marks = {}
subject_marks = {}
skipped_rows = 0

try:
    with open("exams.csv", "r", newline="", encoding="utf-8-sig") as file:

        first_line = file.readline()
        file.seek(0)

        if ";" in first_line and "," not in first_line:
            delimiter = ";"
        else:
            delimiter = ","

        reader = csv.DictReader(file, delimiter=delimiter)

        if reader.fieldnames:
            reader.fieldnames = [
                field.strip().lower() for field in reader.fieldnames
            ]

        if not reader.fieldnames or not all(
            field in reader.fieldnames
            for field in ["name", "subject", "marks"]
        ):
            print("CSV header found:", reader.fieldnames)
            raise ValueError("Please check your CSV header.")

        for row in reader:
            try:
                name = row["name"].strip()
                subject = row["subject"].strip()
                marks = int(row["marks"].strip())

                if not name or not subject:
                    raise ValueError

                if marks < 0 or marks > 100:
                    raise ValueError

                if name not in student_marks:
                    student_marks[name] = []

                student_marks[name].append(marks)

                if subject not in subject_marks:
                    subject_marks[subject] = []

                subject_marks[subject].append(marks)

            except (ValueError, AttributeError, KeyError):
                skipped_rows += 1

    student_averages = {}

    with open("report.txt", "w", encoding="utf-8") as report:

        report.write("EXAM RESULTS REPORT\n")
        report.write("===================\n\n")

        report.write("STUDENT RESULTS\n")
        report.write("-------------------\n")

        for name, marks_list in student_marks.items():

            total = sum(marks_list)
            average = total / len(marks_list)

            student_averages[name] = round(average, 2)

            report.write(f"Student: {name}\n")
            report.write(f"Total Marks: {total}\n")
            report.write(f"Average Marks: {average:.2f}\n\n")

        report.write("SUBJECT RESULTS\n")
        report.write("-------------------\n")

        for subject, marks_list in subject_marks.items():

            average = sum(marks_list) / len(marks_list)
            highest = max(marks_list)
            lowest = min(marks_list)

            report.write(f"Subject: {subject}\n")
            report.write(f"Average: {average:.2f}\n")
            report.write(f"Highest Marks: {highest}\n")
            report.write(f"Lowest Marks: {lowest}\n\n")

    with open("report.json", "w", encoding="utf-8") as file:
        json.dump(student_averages, file, indent=2)

    if student_averages:

        top_student = max(
            student_averages.items(),
            key=lambda item: item[1]
        )

        print(f"Top Student: {top_student[0]}")
        print(f"Average Marks: {top_student[1]}")

    print(f"Skipped Rows: {skipped_rows}")
    print("Reports created successfully.")

except FileNotFoundError:
    print("Error: exams.csv file was not found.")

except ValueError as e:
    print("Error:", e)
