import movie

class MovieList:

  movies = []

  #adds provided movie to list
  def addMovie(self, movie):
    self.movies.append(movie)

  #prints every movie in list
  def printMovieList(self):
    for i in self.movies:
      print(i.getMovieTitle())

  #prints movie at specific index
  def printMovieAtIndex(self, index):
    print(self.movies[index-1].printMovie())

  #returns size of list
  def getSize(self):
    return len(self.movies)

#end movieList class