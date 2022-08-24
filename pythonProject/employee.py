class Employee:
    def __init__(self,fname,lname,address):
        self.firstname=fname
        self.lastname=lname
        self.address=address
    def getfullname(self):
        return self.firstname + ' ' +self.lastname + ' ' +self.address
    def getinitials(self):
        return self.firstname[0] + self.lastname[0]
emp1=Employee("Gowthami","Bandi","Guntur")
emp2=Employee("Gowthami","Bandi","Guntur")
fullname=emp1.getfullname()
print(fullname)
initial=emp1.getinitials()
print(initial)

