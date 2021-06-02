"""A standalone script that retrieves and stores into CSV file report.csv
name of the student who completed homework, data of the creation,
name of the teacher who created homework for all completed homeworks.
"""
import csv

from homework12.models import HomeworkResult, session

results = session.query(HomeworkResult).all()

with open("homework12/report.csv", "w") as report:
    writer = csv.writer(report)
    for result in results:
        student = str(result.author)
        created = str(result.created).split()[0]
        teacher = str(result.homework.teacher)
        writer.writerow((student, created, teacher))

session.close()
