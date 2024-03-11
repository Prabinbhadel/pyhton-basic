class library:
    books={
        "c_programming":10,
        "python":10,
        "stat":10
    }
    borrowed_books={}
    def __init__(self,name):
        self.name=name
    def show_books(self):
        print(f"the books available are: ")
        print(self.books)
    def add_books(self):
        book_name=input("enter the name of the book")
        book_num=int(input("how many do you want to add"))
        self.books[book_name]=book_num
    def borrow_book(self):
        book_name=input("enter the name of the book to be borrowed")
        if(book_name in self.books and self.books[book_name]!=0):
            student=input("enter the name of student that want to borrow the book")
            self.books[book_name] -= 1
            self.borrowed_books[student]=book_name
            print(f"{book_name} book has been borrowed to {student}")
        else:
            print("the requested book is unavailable")
    def return_book(self):
        student=input("enter the name of the student that want to return the book")
        book_name=input("enter the name of the book to return")
        self.books[book_name] += 1
        self.borrowed_books.pop(student)
        print("the book has been returned")
    def display_borrowed_books(self):
        print(self.borrowed_books)


my_library=library("my_library")
while True:
    choice=int(input("1. show the books in library \n 2. add the books in the library \n 3. borrow the books \n 4. return the books \n 5. display the students that have borrowed the books \n 6. exit \n Enter your choice: "))

    if choice==1:
        my_library.show_books()
    if choice==2:
        my_library.add_books()
    if choice==3:
        my_library.borrow_book()
    if choice==4:
        my_library.return_book()
    if choice==5:
        my_library.display_borrowed_books()
    if choice==6:
        break

