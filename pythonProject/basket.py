from leave import Leave
class BasketOfLeave(Leave):
    def _init_(self, Employeeid, Name, LeaveBalance, Applyingleave):
        super()._init_(Employeeid,Name,LeaveBalance)
        self.Applyingleave=Applyingleave

    def displayleave(self):
        return self.LeaveBalance-self.Applyingleave