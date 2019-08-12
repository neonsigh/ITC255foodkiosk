from customer import Customer
from menu import Menu
from orderinfo import OrderInfo
from order import Order
from payment import Payment

def setCustomer():
    c=Customer('Chris')
    print(c)

def main():
    setCustomer()
    option1=Menu(1, 'Plat du Jour', 11.50)
    option2=Menu(2, 'Entree et Plat', 15.00)
    option3=Menu(3, 'Plat et Dessert', 15.00)
    option4=Menu(4, 'Cafe au Lait', 3.00)

    orderinfo1=OrderInfo(option1,1)
    orderinfo2=OrderInfo(option2,2)
    orderinfo3=OrderInfo(option3,3)
    orderinfo4=OrderInfo(option4,4)

    order=Order()
    order.addItem(orderinfo1)
    order.addItem(orderinfo2)
    order.addItem(orderinfo3)
    order.addItem(orderinfo4)

    payment=order.subtotal()
    print(payment)

main()