from tdd_lesson.GradeBook import GradeBook
from tdd_lesson.Subject import Subject

def run_main():
    grade_book=GradeBook()
    math=Subject("Matematyka")
    art=Subject("Sztuka")
    grade_book.add_subject(math)
    grade_book.add_subject(art)
    grade_book.add_grade(math,3)
    grade_book.add_grade(math, 3)
    grade_book.add_grade(math, 4)
    grade_book.add_grade(art, 5)
    grade_book.add_grade(art, 6)
    print(grade_book.grades_book)
    print(f"średnia ocen z matematyki: {math.get_average_grades():.2f}")
    print(f"średnia ocen ze sztuki: {art.get_average_grades()}:.2f")
    print(f"średnia wszystkich ocen: {grade_book.add_average()}")




if __name__=="__main__":
    run_main()