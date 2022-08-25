class Leave:
    def __init__(self,employee_id,name,leavebalance):
        self.id=employee_id
        self.name=name
        self.leavebalance=leavebalance
    def display(self):
        return self.id,self.name,self.leavebalance

