from menu import Menu
from orderinfo import OrderInfo
from payment import Payment

class Order():
    def __init__(self):
        self.orderinfoList=[]

    def addItem(self, orderinfo):
        self.orderinfoList.append(orderinfo)

    def subtotal(self):
        subtotal=0.0
        for o in self.orderinfoList:
            subtotal += o.getMenuItem().itemPrice*o.quantity
        payment=Payment(subtotal,0.1)
        return payment