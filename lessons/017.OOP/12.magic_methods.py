# double under score methods inside a class automaticaly called by python's build in operators
# allow dev to customize the behaviour of an object
# for example if you want to customize the behaviour of the print function when called on an object you can use the __str__ method
# like operator overloading in cpp


class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # by default when you call the print method it returns the memory addres of the created Object
    # We can change this by cusutomizing the __str__ method
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # by default 2 objects of the same class can not be equal as they ocupy diffrent places in memory
    # but we can customize this to make sure the eqaulity checks the title and autor
    def __eq__(self, value):
        return self.title == value.title and self.author == value.author

    # normaly we can not use less than on an object of book but we can change this
    def __lt__(self, other):
        return self.num_pages < other.num_pages

    # greater than
    def __gt__(self, other):
        return self.num_pages > other.num_pages

    # when we add 2 obj instances
    def __add__(self, other):
        return self.num_pages + other.num_pages

    # when we search using the in keword
    def __contains__(self, item):
        return item in self.title or item in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"


book1 = Book("The song of ice and fire", "J.R.R", 310)
book2 = Book("IT", "J.R.R", 223)
book3 = Book("The lion", "C.S lewis", 172)


print(book1)  # will return 'The song of ice and fire' by J.R.R
print(book2)  # will print 'IT' by J.R.R


book4 = Book("The song of ice and fire", "J.R.R", 205)

print(
    book1 == book4
)  # True as we already changed the __eq__ behavour to just compare title and author not the memory location


print(book1 < book4)  # false as we changed the behaviour of the __lt__
print(book1 > book4)  # True wa changed the __gt__


print(book1 + book4)  # 515 it adds as we customize the addition behaviour __add__


print("lion" in book3)  # true as we customized the __contains__ method


print(
    book1["title"]
)  # the subscript operator is not usable by default but we customized the __getitem__ method
