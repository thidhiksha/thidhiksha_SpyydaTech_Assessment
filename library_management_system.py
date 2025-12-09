#library management
#create class
class LibrarySystem:
  def __init__(self):
    self.books={}
    #add book
  def add_book(self):
    name = input("Enter Book Name:")
    self.books[name]="Available"
    print("Book added")
    #search book
  def search_book(self):
    name = input("Enter book name to search:")
    if name in self.books:
        print(f"Status: {self.books[name]}")
    else:
      print("Book not found")
      #borrow book
  def borrow_book(self):
      name= input("Enter book name to borrow:")
      if name in self.books and self.books[name]=="Available":
          self.books[name]="Borrowed"
          print("You borrowed the book")
      else:
          print("Book not available")
        #return book
  def return_book(self):
      name = input("Enter book name to return:")
      if name in self.books:
          self.books[name]= "Available"
          print("Book returned")
      else:
          print("Book doesn't exist")
        #menu
  def menu(self):
      while True:
          print("\n1.Add 2.Search 3.Borrow 4.Return 5.Exit")
          choice = input("Choose option:")
#choice
          if choice=="1":
            self.add_book()
          elif choice=="2":
            self.search_book()
          elif choice=="3":
            self.borrow_book()
          elif choice=="4":
            self.return_book()
          elif choice=="5":
            break
          else:
              print("Invalid Input")
if __name__=="__main__":
    LibrarySystem().menu()
