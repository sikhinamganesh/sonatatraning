from leave import Leave

class Basketofleave(Leave):
    def __init__(self,employee_id,name,LeaveBalance,applyingleave):
        super().__init__(employee_id,name,LeaveBalance)
        self.applyingleave=applyingleave
    def displayLeave(self):
        return self.Leavebalance-self.applyingleave