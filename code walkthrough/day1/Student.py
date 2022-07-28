 #creating a student class 
class Student: 
    
    def __init__(self, name, major, gpa): 
        self.name = name 
        self.major = major 
        self.gpa = gpa

# can also put functions in class
#for object func, self has to be first parameter
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else: 
            return False