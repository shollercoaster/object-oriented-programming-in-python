class Fraction():
    def __init__(self, num, den = 1):
        if den < 0:
            new_num =  -num
            new_den = -den
            self.nr = new_num
            self.dr = new_den
        else:
            self.nr = num
            self.dr = den
        
    def multiply1(self, nr1, nr2, dr1 = 1, dr2 = 1):
#        self.nr = nr1 * nr2
#        self.dr = dr1 * dr2
        product = self * fraction 
        return product
    
    def multiply(self, fraction):
        new_nr = self.nr * fraction
        new_dr = fraction / self.dr
        product = Fraction(new_nr, new_dr)
        return product.display()

    def display(self):
        print(self.nr, "/", self.dr)
        
fr = Fraction(2,-3)
fr.display()
product = fr.multiply(2/3)
print("product", product)