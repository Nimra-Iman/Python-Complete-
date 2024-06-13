class Library:
    # def __init__(self,no_of_books,books):
    #     self.books=books
    #     self.num=no_of_books

    def showBooks(self):
        f=open("LMS.txt","r")
        print(f.read())
        f.close()

    def add_book(self,text):
        with open("LMS.txt","a") as f:
            f.write(text+"\n")

    def count_books(self):
        i=0
        with open("LMS.txt","r") as f:
            while True:
                line=f.readline() 
                i=i+1
                if not line:
                    print(i-1)
                    break
obj=Library()
while True:
    choose=(input("1- to know total number of books\n2- to show all books\n3- add a book\n OR PRESS 'exit' TO EXIT"))

    if(choose=="2"):
       obj.showBooks()
    if(choose=="3"):
        write_book_name=input("add your book here")
        obj.add_book(write_book_name)
    if(choose=="1"):
        obj.count_books()

    if (choose=="exit" ):
        break

print("THANKS FOR VISITING OUR LIBRARY")