class Product():
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self.discount = discount
        
    @property
    def selling_price(self):
        return self.marked_price - ((self.discount/100) * self.marked_price)
    
    @property
    def discount(self):
        return self._discount + 2 if self.marked_price > 500 else self._discount
    
    @discount.setter
    def discount(self, new_discount):
        self._discount = new_discount
    
    def display(self):
        print(self.id,  self.marked_price,  self.discount)
    
p1 = Product('X879', 400, 6)
p2 = Product('A234', 100, 5)
p3 = Product('B987', 990, 4)
p4 = Product('H456', 800, 6)
print(p1.selling_price)
print(p3.discount)
p4.display()