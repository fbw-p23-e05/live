

# Dunder/Magic methods


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author


    def best_seller(self):
        return f'{self.title} by {self.author} is a best seller.'
    

    def __str__(self):
        return f'{self.title} by {self.author}'
    

    def __repr__(self):
        return f'{self.title} by {self.author}'
    

    def __len__(self):
        return len(self.title) + len(self.author)
    

book_1 = Book('Python for Beginners', 'James Brown')

# print(book_1.__str__())
# print(book_1.__repr__())
# print(len([22, 33, 444, 555]))
# print(len(book_1))


# Operator Overloading


class Calculator:

    def __init__(self, number):
        self.number = number

    def __add__(self, other_object):
        self.other_object = other_object
        return self.number + self.other_object.number
    

    def __mul__(self, other_obj):
        self.other_obj = other_obj
        return self.number * self.other_obj.number
    
    # def __sub__(self, other_obj1, other_obj2):
    #     self.other_obj1 = other_obj1
    #     self.other_obj2 = other_obj2

    #     return self.number - self.other_obj1.number - self.other_obj2.number
    
    # def __sub__(self, other_obj):
    #     self.other_obj = other_obj

    #     return self.number - self.other_obj.number

    def add_number(self, *args):
        self.args = args

        total = 0

        for arg in args:
            self.arg += arg

        return total
    
    def __lt__(self, obj):
        self.obj = obj
        return self.number < self.obj.number


calc_1 = Calculator(300)
calc_2 = Calculator(400)
calc_3 = Calculator(700)




# print(calc_1.__add__(10, 40, 2, 70, 2000))
# print(calc_1 + calc_2 + calc_3)

# __eq__, __lt__, __gt__

print(calc_1 < calc_2)

# print(3 * 10)
# print(300 + 400)
# print(calc_1 + calc_2)
# print(700 - 400 - 300)
# # print(calc_3.__sub__(calc_2, calc_1))

# print((calc_3 - calc_2) - (calc_2 - calc_1))

# print(calc_1.__mul__(calc_2))

# print(3.__mul__(10))



    # def __add__(self, number2):
    #     self.number2 = number2
    #     return self.number + self.number2
         
        
        # return self.number + self.other_object
                # 300        +  400


# 300.__add__(400)
# calc_1.__add__(calc_2)



# calc_3 = Calculator(800)

# print(300 + 400)
# print(calc_1 + calc_2)

# print(calc_1.__add__(400))
# print(calc_2)



        






