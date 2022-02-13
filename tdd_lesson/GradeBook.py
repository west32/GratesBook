from Subject import Subject

class GradeBook():
    def __init__(self,grades_book=None):
        if grades_book is None:
            grades_book = {}
        self.grades_book= grades_book



    def add_subject(self,subject):

        if subject.name in self.grades_book.keys():
            raise Exception('Dany przedmiot już jest w dzienniku')

        else:
            self.grades_book[subject.name]=subject.grades
            return self.grades_book


    def get_subject(self, subject):
        for element in self.grades_book.keys():
            if element == subject:
                return  subject.name

    def add_grade(self,subject,grade):

        return subject.grades.append(grade)

    def add_average(self):
        values_sum=0
        values_counter=0

        for value in self.grades_book.values():
            for element in value:
                values_counter +=1
                values_sum +=element
        return values_sum / values_counter



