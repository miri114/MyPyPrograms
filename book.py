class Book():

    def __init__(self, title, author, price, width):
        self.title = title
        self.author = author
        self.price = price
        self.width = width

class Shelf():

    def __init__(self, shelf_width):
        self.books = []
        self.shelf_width = shelf_width

    def add_book(self, *new_books):
        for one_book in new_books:
            if one_book.width > 15:
                try:
                    raise ValueError("Book greater than shelf ")
                except ValueError as vl:
                    print(vl)
            else:
                self.books.append(one_book)

        # try:
        #     [self.books.append(one_book) if one_book.width < self.shelf_width else
        #      print("Book width is greater than the shelf's") for one_book in new_books]
        # except ValueError:
        #     print("It has an error")

    def total_price(self):
        return sum(item.price for item in self.books)

    def has_book(self, titull):
        return bool(titull in (t.title for t in self.books))

    def __repr__(self):
        return '\n'.join(f'{item.title} {item.author} {item.price} {item.width}' for item in self.books)


b1 = Book('test1', 'test1', 10, 10)
b2 = Book('test2', 'test2', 25, 15)
b3 = Book('test3', 'test3', 25, 20)

my_shelf = Shelf(15)
my_shelf.add_book(b1)
my_shelf.add_book(b2, b3)

print(my_shelf)
print(my_shelf.has_book("Miri"))