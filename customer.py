class Customer():
    def __init__(self,name):
        self.custName=name

    def getName(self):
        return self.custName

    def __str__(self):
        return self.custName