class Subject():


    def __init__(self,name,grades=None):
        self.name=name
        if grades is None:
            grades = []
        self.grades=grades

    def get_subject(self):
        return self.name

    def get_average_grades(self):
        avg=sum(self.grades)/len(self.grades)
        return avg