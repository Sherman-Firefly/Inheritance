class employee:
    def __init__(self,name,empid):
        self.name=name
        self.empid=empid
        

    def details(self):
        print("Employee name: ", self.name)
        print("Employee ID: ", self.empid)

class HR(employee):
    def __init__(self, name, empid, position):
        super().__init__(name, empid)
        self.position=position

    def details(self):
        super().details()
        print("Position:", self.position)

newemployee=employee("Bob", "S10284")
newemployee.details()

print("\n\n\n\n")

man=HR("Dave", "H21134", "Councilor")
man.details()
