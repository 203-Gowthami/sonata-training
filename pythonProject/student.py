class Student:
    def __init__(self,student_id,student_name):
        self.student_id=student_id
        self.student_name=student_name
    def getstddet(self):
        return self.id,self.student_name
std1=student(22796,'Gowthami')
display=std1.getstd
