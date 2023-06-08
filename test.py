from entities.book import Book
import csv

books = []

with open('books.csv', 'r+') as csv_file :
  reader = csv.reader(csv_file)
  primeira_linha = True # Boolean

  for row in reader :
    if primeira_linha : primeira_linha = False
    else : books.append( Book(name = row[1], author = row[2], release_year = row[3], price = row[4]) )

for book in books : print(book)
