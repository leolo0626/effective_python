from GradeBook import GradeBook


book = GradeBook()
leo = book.get_student("Leo")
math = leo.get_subject('Math')
math.report_grade(75, 0.05)
math.report_grade(85, 0.15)
math.report_grade(70, 0.8)

print(leo.average_grade())