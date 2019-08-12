class Menu():
    def __init__(self, itemNum, itemName, itemPrice):
        self.itemNum=itemNum
        self.itemName=itemName
        self.itemPrice=itemPrice

    def getItemNum(self):
        return self.itemNum

    def getItemName(self):
        return self.itemName

    def getItemPrice(self):
        return self.itemPrice

    def __str__(self):
        return self.itemName


