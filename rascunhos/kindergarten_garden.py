class Garden:

    DEFAULT_STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
    PLANTS = {'C': 'Clover', 'G': 'Grass', 'R': 'Radishes', 'V': 'Violets'}
    def __init__(self, diagram, students=None):
        self.rows = diagram.splitlines()
        garden_length = len(self.rows[0])
        if students is None:
            self.students = Garden.DEFAULT_STUDENTS
        else:
            self.students = sorted(students)
        self.student_flowers = {}
        for count, student in enumerate(self.students):
            if (count + 1) * 2 > garden_length:
                break
            else:
                student_plants = []
                for row in self.rows:
                    student_plants.append(row[count * 2])
                    student_plants.append(row[count * 2 + 1])
                plants = [Garden.PLANTS[plant] for plant in student_plants]
                self.student_flowers[student] = plants
    def plants(self, student):
        return self.student_flowers[student]
