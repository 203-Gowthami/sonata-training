from employee import Employee
from address import Address
address1=Address("banglore",53567)
address2=Address("hyderabad",87665)

emp1=Employee("Gowthami","Bandi","Guntur")
emp2=Employee("Gowthami","Bandi",[address1,address2])
print(address1.city)
print(address2.pincode)
