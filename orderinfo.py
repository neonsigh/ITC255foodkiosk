from menu import Menu
import datetime

orderDate=datetime.datetime.now()

class OrderInfo():
    def __init__(self, menu, quantity):
        self.datetime=orderDate
        self.menu=menu
        self.quantity=quantity
        
    def getDatetime(self):   
        return self.datetime

    def getMenuItem(self):
        return self.menu

    def getQuantity(self):
        return self.quantity

    
    