def gradingStudents(grades):
    return [grade + 5 - grade % 5 if grade > 37 and 5 - grade % 5 < 3 else grade for grade in grades]


print(gradingStudents([73, 67, 38, 33]))
