class Person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def persondetails(self):
        print("my name is",self.name,"my id number is ",self.idnumber)
obj1=Person("mahesh","19837")
obj1.persondetails()
