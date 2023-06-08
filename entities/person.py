import book_manager

class User :

  def __init__(self, username, password, books, balance) :
    self.username = username
    self.password = password
    self.books = books
    self.balance = float(balance)
  
  def buy (self, book) :
    if self.balance >= book.price : 
      self.balance -= book.price
      self.books.append(book);
    else :
      print('not enought balance')

  def buy (name, author):
    book = book_manager.findByNameAndAuthor(name, author)