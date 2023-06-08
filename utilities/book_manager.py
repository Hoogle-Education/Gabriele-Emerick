def findByNameAndAuthor(books, name, author) :
  list = []

  for book in books:
    if (book.name == name) and (book.author == author):
      list.append(book)
  
  return list