
class Book():
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies
        
    def in_stock(self):
        flag = True if self.copies > 0 else False
        return flag
    
    def sell(self):
        if self.copies > 0:
            self.copies -= 1
        else:
            print("this book is out of stock.")
            
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if 50 < new_price < 1000 :
            self._price = new_price
        else:
            raise ValueError('the price of a book cannot be less than 50 or more than 1000.')
        
    def display(self):
        print(f"isbn: {self.isbn} title: {self.title}, price: {self.price} and number of copies of the book: {self.copies}.")
        
        
book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

books = [book1, book2, book3, book4]
for i in books:
    i.display()
    
jack_books = [x.title for x in books if x.author == 'Jack']
print("jack ki books: ", jack_books)

#book1.display()
#book2.display()
#book3.display()
#book4.display()
copies = book3.in_stock()
print("product in stock: ", copies)
book2.sell()
book2.display()