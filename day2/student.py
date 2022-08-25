class student:
    def __init__(self,student_id,student_name):
        self.id=student_id
        self.name=student_name
    def addstu(self):
        return self.id,self.name
a=student(654321,"ganesh")
b=a.addstu()
print(b)
setattr(a,'student_class',13)
print(getattr(a,'student_class'))
delattr(a,'name')
print(hasattr(a,'student_name'))
#print(hasattr(a,'student_name'))
a=student(654321,'ganesh')
b=a.addstu()
print(b)