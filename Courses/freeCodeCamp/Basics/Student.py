class Student:

    def __init__(self, name, major, gpa, is_abroad):  # we can map out students' attributes here
        self.name = name  # the object's name is going to be equal to the name that we enter
        self.major = major  # the student's major is going to be equal to the major that we pass in
        self.gpa = gpa
        self.is_abroad = is_abroad

    def on_honor_roll(self):
        # the actual student's gpa = self.gpa
        if self.gpa >= 9.5:
            return True
        else:
            return False

