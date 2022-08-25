class employee:
    def __init__(self,employee_id,employee_name):
        self.id=employee_id
        self.name=employee_name
    def addstu(self):
        return self.id,self.name
a=employee(654321,"ganesh")
b=a.addstu()
print(b)
