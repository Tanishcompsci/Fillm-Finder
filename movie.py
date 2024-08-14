import locale

class Movie:

  locale.setlocale( locale.LC_ALL, '' ) #used to format currency
  
  #constructor
  def __init__(self, title, revenue, budget, voteAverage, releaseDate):
    
    self.title = title
    self.revenue = revenue
    self.budget = budget
    self.voteAverage = voteAverage
    self.releaseDate = releaseDate

  #returns movie title
  def getMovieTitle(self):
    return self.title

  #returns movie revenue
  def getMovieRevenue(self):
    return self.revenue

  #returns movie budget
  def getMovieBudget(self):
    return self.budget

  #returns average of movie reviews on scale of 1-10
  def getMovieReviews(self):
    return self.voteAverage

  #returns movie release date
  def getMovieReleaseDate(self):
    return self.releaseDate

  #this method is used to print a film's attributes when the user wishes to view them
  def printMovie(self):
    return "\n" + str(self.title) + "\nRelease Date: " + str(self.releaseDate) + "\nReviews: " + str(self.voteAverage) + "\nBudget: " + str(locale.currency(self.budget, grouping=True)) + "\nBox Office: " + str(locale.currency(self.revenue, grouping=True))

  '''
  The following method returns all the film's attributes in a comma-separated line. The method is used when the user decides to place a movie in their favorites list. A text file is opened and the method is used to appended to the file.
  '''

  def getMovie(self):
    return str(self.title) + ', ' + str(self.voteAverage) + ', ' + str(self.releaseDate) + ', ' + str(self.budget) + ', ' + str(self.revenue)

#end movie class
