
class Grade:
    __min__ = 0
    __max__ = 100

    def __init__(self, mark):
        self.mark = mark


class Assignment:

    def __init__(self, name, text, rate, deadline):
        self.name = name
        self.text = text
        self.rate = rate
        self.deadline = deadline


class AssignmentGrade:

    def __init__(self, course, assignment, mark):
        self.course = course
        self.assignment = assignment
        self.grade = Grade(mark)
        self.state = 0


class User(object):

    def __init__(self, firstname, lastname,  id, username, password, email):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.username = username
        self.password = password
        self.email = email


class Student(User):

    def __init__(self, firstname, lastname,  id, username, password, email):
        User.__init__(self, firstname, lastname,  id, username, password, email)
        self.courses = []
        self.assignmentgrades = []

    def displayinfo(self):
        print "The courses for the student: " + self.firstname + " " + self.lastname + "   with id: " + self.id + " are: "
        for course in self.courses:
            print course.name + " - " + course.id + " - lecturer name: " + course.lecturer
        for key in self.assignmentgrades:
            print "The assignments for " + key.course.name + " are: "
            print key.assignment.name + ": " + str(key.grade.mark)


class Lecturer(User):
    def __init__(self, firstname, lastname,  id, username, password, email):
        User.__init__(self, firstname, lastname,  id, username, password, email)


class Course:

    def __init__(self, name, id, lecturer):
        self.name = name
        self.id = id
        self.lecturer = lecturer
        self.assignments = []


def main():
    c1 = Course("Data Structures", "ENGS115", "Satenik Mnatskanyan")
    c2 = Course("Linear Algebra", "ENGS103", "Gayane Ghazaryan")
    st1 = Student("Sarkis", "Kabrailian", "m94968683", "Sarkis007", "******", "Sarkis_kabrailian@edu.aua.am")
    asgn1 = Assignment("Assignment1", "Assign1Text", 50, "2018-09-10")
    asggrade1 = AssignmentGrade(c1, asgn1, 100)
    asgn2 = Assignment("Assignment2", "Assign2Text", 50, "2018-09-16")
    asggrade2 = AssignmentGrade(c1, asgn2, 90)
    c1.assignments.append(asgn1)
    c1.assignments.append(asgn2)
    st1.courses.append(c1)
    st1.courses.append(c2)
    st1.assignmentgrades.append(asggrade1)
    st1.assignmentgrades.append(asggrade2)
    st1.displayinfo()


main()

