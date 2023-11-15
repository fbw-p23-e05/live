class Book:
    
    def __init__(self, name, author, price, qty=1):
        self.name = name
        self.author = author
        self.price = price
        self.qty = qty


    def get_name(self):
        return self.name
    

    def get_author(self):
        return self.author
    

    def get_price(self):
        return self.price
    
    def set_price(self, new_price):
        self.price = new_price


    def get_qty(self):
        return self.qty
    

    def set_qty(self, quantity):
        self.qty = quantity

    def get_author_name(self):
        return self.author._name
    
    def get_author_email(self):
        # return self.author.__email
        return self.author.get_email()


    def __str__(self):
        return f'Book[name={self.name},Author[name={self.author._name},email={self.author.get_email()},gender={self.author._gender}],price={self.price},qty={self.qty}]'



