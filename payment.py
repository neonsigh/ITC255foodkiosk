class Payment():
    def __init__(self, subtotal, taxpercent):
        self.subtotal=subtotal
        self.tax=subtotal*taxpercent
        self.total=subtotal+self.tax

    def __str__(self):
        self.subtotal=round(self.subtotal, 2)
        self.tax=round(self.tax, 2)
        response="Subtotal: $" + str(self.subtotal) + '\n' + "Tax: $" + str(self.tax) + '\n' + "Total: $" + str(self.total)
        return response

    
    
