import requests
import locale
import sys
import subprocess
from movie import Movie
from movieList import MovieList

#login variables
username = ""
password = ""
isUser = False

continuePgm = "y" #used to determine when program should end
movieList = MovieList() #user's favorite movies are added to movieList
locale.setlocale( locale.LC_ALL, '' ) #used to format currency

print("Welcome to Film Finder!\n\n")

#repeats while user is not logged in
while (isUser == False):
 
  accountOption = input("Enter 'L' to login or 'R' to register for an account: ")

  if (accountOption == "L" or accountOption == "l"):
    username = input("Username: ")
    password = input("Password: ")
    users = open("users.txt", "r")
    userList = users.readlines()

    #determines if username/password is in 'users.txt'
    for i in userList:
      if username in i and password in i:
        isUser = True
    users.close()

    #returns to login page if login credentials are invalid
    if (isUser == False):
      print("\nNo account registered with those credentials.")

  #register new account
  elif (accountOption == "R" or accountOption == "r"):
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    users = open("users.txt", "a")

    #adds user information to 'users.txt'
    users.write("\n" + username + " " + password)
    users.close()
    subprocess.call(['clear'])  #clear console
    isUser = True

#repeats when user chooses to continue browsing 
while (continuePgm == "y" or continuePgm == "Y"):
  subprocess.call(['clear'])  # clear console

  print("Welcome back,", username + "!")

  #menu list
  print("\nWhat would you like to do?")
  choice = int(
      input(
          "\n1. Browse movies\n2. Display your favorite movies\n3. Exit\n> ")
  )

  #search for movies
  if (choice == 1):
    subprocess.call(['clear'])  # clear console
    movieTitle = input("Enter a movie title: ")

    #uses API key to search for movie title
    apiKey = "0fc076e8f6e21a94b2a7e154b0a82811"
    searchUrl = f'https://api.themoviedb.org/3/search/movie?api_key={apiKey}&query={movieTitle}'

    response = requests.get(searchUrl)
    data = response.json()
    
    if data['results']:  # checks if query results exist

      #get attributes of the first movie in query results

      #movie ID is used to construct URL to fetch movie information
      movieID = data['results'][0]['id']
      idURL = f'https://api.themoviedb.org/3/movie/{movieID}?api_key={apiKey}'
      response = requests.get(idURL)
      data = response.json() #store response as json

      #print movie title
      movieTitle = data['title']
      print(f"\nMovie: '{movieTitle}'")

      #print release date
      releaseDate = data['release_date']
      print(f"Release date: {releaseDate}")

      #print movie reviews
      reviews = data['vote_average']
      print(f"User consensus review: {reviews}/10")

      #print movie box office
      boxOffice = data['revenue']
      print(f"Box office: {locale.currency(boxOffice, grouping=True)}")

      #print budget
      budget = data['budget']
      print(f"Budget: {locale.currency(budget, grouping=True)}")

      isFavorite = input("\nIs this one of your favorite movies? (y/n): ")

      #adds movie to list if it's a favorite
      if (isFavorite == "y" or isFavorite == "Y"):

        #creates movie object with selected film information

        movieParam = Movie(movieTitle, boxOffice, budget, reviews, releaseDate)

        #adds object to movieList
        movieList.addMovie(movieParam)

        #appends to file with list of user's favorite movies
        fileName = username + ".txt"
        userFavorites = open(fileName, "a")
        userFavorites.write(movieParam.getMovie() + "\n")

        print("'" + movieTitle + "' was added to your favorites list.")

    #returns error message if no query results are found
    else:
      print("Title not found")

  #printing movie list
  elif (choice == 2):

    fileName = username + ".txt"

    #print user's favorite movies and add to list class
    try:
      userFavorites = open(fileName, "r")
      userList = userFavorites.readlines()

      subprocess.call(['clear'])  # clear console
      print("Your favorite movies:")
      count = 0

      for i in userList:

        #store film's attributes
        attributes = i.strip().split(',')
        movieTitle = attributes[0]
        ratingIndex = attributes[1]
        releaseDateIndex = attributes[2]
        budgetIndex = attributes[3]
        boxOfficeIndex = attributes[4]

        #create movie object and add to list
        movieParam = Movie(movieTitle, boxOfficeIndex, budgetIndex,
                           ratingIndex, releaseDateIndex)
        movieList.addMovie(movieParam)
        count += 1
        print(str(count) + ". " + movieTitle)

      #allows user to view detailed information about their favorite movies
      viewMovie = input("\nWould you like to view movie details? y/n: ")
      if (viewMovie == "y" or viewMovie == "Y"):
        whichMovie = -1
        
        while(whichMovie > movieList.getSize() or whichMovie < 1):
          whichMovie = int(input("Select a movie from the numbered list above: "))

          #prints movie at specified index of list
          if(whichMovie <= movieList.getSize()):
            print(movieList.printMovieAtIndex(whichMovie))

          else:
            print("That index does not exist")

    #error-trapping if user has no movies in list
    except:
      print("You have no movie entries in this list.")

  #exits program
  elif (choice == 3):
    print("Goodbye", username + "!")
    sys.exit(0)

  #error traps value outside of accepted range
  else:
    print("That option does not exist.")

  continuePgm = input("\nConinue browsing? (y/n): ")

#prints if user stops browsing
print("Goodbye!")

'''
OUTPUT (Not Including Console Clears)

Welcome to Film Finder!


Enter 'L' to login or 'R' to register for an account: L
Username: Tanish
Password: Parlapall

Welcome back, Tanish!

What would you like to do?

1. Browse movies
2. Display your favorite movies
3. Exit
> 1

Enter a movie title: Avengers: Endgame

Movie: 'Avengers: Endgame'
Release date: 2019-04-24
User consensus review: 8.255/10
Box office: $2,800,000,000.00
Budget: $356,000,000.00

Is this one of your favorite movies? (y/n): y
'Avengers: Endgame' was added to your favorites list.

Coninue browsing? (y/n): y

Welcome back, Tanish!

What would you like to do?

1. Browse movies
2. Display your favorite movies
3. Exit
> 2
Your favorite movies:
1. Avengers: Endgame

Would you like to view movie details? y/n: y
Select a movie from the numbered list above: 1

Avengers: Endgame
Release Date: 2019-04-24
Reviews: 8.255
Budget: $356,000,000.00
Box Office: $2,800,000,000.00
None

Coninue browsing? (y/n): y

Welcome back, Tanish!

What would you like to do?

1. Browse movies
2. Display your favorite movies
3. Exit
> 3
Goodbye Tanish!

'''