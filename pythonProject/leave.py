class Leave:
   def _init_(self,Employeeid,Name,LeaveBalance):
        self.employeeid=Employeeid
        self.name=Name
        self.leavebalance=LeaveBalance
   def display(self):
        return self.employeeid,self.name,self.leavebalance
