class Students:
    def __init__(self, name,course,gender,age):
        self.name=name
        self.course=course
        self.gender=gender
        self.age=age

    def display(self):
        print(f"Name : %s\n Course :%s \nGender : %s\n Age: %d"
             % (self.name,self.course,self.gender,self.age))

stud1= Students("Lucky Muye",
                "Computer Science","Male",31)
stud2=Students("Mercy Moringa","Software engineer","Female",40)
stud1.display()
stud2.display()