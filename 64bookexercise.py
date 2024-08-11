class library:
    def __init__(self):
        self.nobooks=0
        self.booklist=[]

    def addbook(self,book):
        self.booklist.append(book)
        self.nobooks = len(self.booklist)

    def showinfo(self):
        print(f"the library has {self.nobooks} books.The books are")
        for book in self.booklist:
            print(book)

l1=library()
l1.addbook("ikigai")
l1.addbook("rd sharma")

l1.showinfo()