class School:
    def __init__(self):
        self.classes = {}
        self.in_school = []
    def add_student(self, name, grade):
        if name not in self.roster():
            self.classes[grade] = self.classes.get(grade, [])+[name]
            self.in_school.append(True)
        else:
            self.in_school.append(False)
    def roster(self):
        student_roster = []
        for grade in sorted(self.classes.keys()):
            for student in sorted(self.classes[grade]):
                student_roster.append(student)
        return student_roster
    def grade(self, grade_number):
        return sorted(self.classes.get(grade_number, []))
    def added(self):
        return self.in_school
