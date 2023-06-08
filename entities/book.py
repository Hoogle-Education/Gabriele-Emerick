
# atributos
# métodos

class Book :

  def __init__(self, name, author, release_year, price) :
    self.name = name
    self.author = author
    self.release_year = int(release_year)
    self.price = float(price)

  def __str__(self):
    return f'Livro: {self.name} , ano: {self.release_year} \npor {self.author} '
    