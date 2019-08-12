import unittest
from menu import Menu
from orderinfo import OrderInfo
from order import Order
from payment import Payment


class MenuTest(unittest.TestCase):
    def setUp(self):
        self.menu=Menu(1,'combo one', 19.00)

    def test_menuString(self):
        self.assertEqual(str(self.menu),self.menu.itemName)

    def test_getItemPrice(self):
        self.assertEqual(str(self.menu.getItemPrice()), '19.0')

    def test_getMenuItemNumber(self):
        self.assertEqual(str(self.menu.getItemNum()),'1')



class OrderInfoTest(unittest.TestCase):
    def setUp(self):
        self.menu=Menu(2,'tacos', 12.00)
        self.quantity=2 
        self.orderinfo=OrderInfo(self.menu, self.quantity)

    def test_getMenuItem(self):
        self.menu = self.orderinfo.getMenuItem()
        self.assertEqual(str(self.menu),'tacos')  

    def test_getItemPrice_OrderInfo(self):
        self.menu = self.orderinfo.getMenuItem()
        self.assertEqual(self.menu.getItemPrice(), 12.00)

    def test_getQuantity(self):
        self.assertEqual(self.orderinfo.getQuantity(),2)

    #not passed
    def test_getQuantityFail(self):
        self.assertEqual(self.orderinfo.getQuantity(),22)


#not passed
class OrderTest(unittest.TestCase):

    def setUp(self):
       self.o=Order()
       self.menuitem1=Menu(3,'beer', 5.00)
       self.menuitem2=Menu(7,'cheesecake', 21.00)

       self.orderitem1=OrderInfo(self.menuitem1,1)
       self.orderitem2=OrderInfo(self.menuitem2,3)

       
       self.o.addItem(self.orderitem1)
       self.o.addItem(self.orderitem2)


    #not passed
    def test_CalculateTotalFail(self):
        payment=self.o.subtotal()
        self.assertEqual(str(payment), 'Total: 49.99')

    def test_getMenuItemFail(self):
        self.menu = self.menuitem1
        self.assertEqual(str(self.menu),'tacos')  

    def test_getItemPriceFail(self):
        self.menu = self.menuitem1
        self.assertEqual(str(self.menu.getItemPrice()), '19.0')

