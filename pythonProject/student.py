class Student:
    def _init_(self,student_id,student_name):
        self.student_id=student_id
        self.student_name=student_name
    def display(self):
        print("student_id:",self.student_id)
        print("student_name:",self.student_name)
obj=Student("22796","Gowthami")
obj.display()
