class Garden:
    
    #Define class variables, i.e., variables that are valid for any object created by the class
    DEFAULT_STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
    PLANTS = {'C': 'Clover', 'G': 'Grass', 'R': 'Radishes', 'V': 'Violets'}

    def __init__(self, diagram, students=None):
        #Define object variables         
        #Check if the student list is diferent from the default list and assign value to the object variable self.student accordingly
        if students is None:
            self.students = Garden.DEFAULT_STUDENTS
        else:
            self.students = sorted(students)
        self.rows = diagram.splitlines()
        garden_length = len(self.rows[0])
        #Dictionary that we will fill with students and their plants
        self.student_flowers = {}


        for count, student in enumerate(self.students):
            #Check if the garden is large enough for all or only some of the students in the list
            if (count + 1) * 2 > garden_length:
                break
            else:
                #To create a list of seeds that the diagram assigns to each student, we must go loop through the two rows in the garden, and find the seeds on the basis of the student position in the students list.
                student_seeds = []
                for row in self.rows:
                    student_seeds.append(row[count * 2])
                    student_seeds.append(row[count * 2 + 1])
                #Use the dictionary to translate the letters in student_seeds to actual plant names in the plant list
                plants = [Garden.PLANTS[seed] for seed in student_seeds]
                #Create a dictionary entry where the value is the student and its key's the list of plants
                self.student_flowers[student] = plants

    def plants(self, student):
        #Use the dictionary to return the list of plants associated with a particular student.
        return self.student_flowers[student]
