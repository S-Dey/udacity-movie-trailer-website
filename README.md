# Movie Trailer Website
## About
The Movie Trailer Website project consists of server-side code to store a list of movies titles, along with its respective box art imagery, and other information about them. The data is served as an HTML Web page allowing visitors to review the movies and watch the trailers.

This project is being created as part of Udacity's Full-Stack Web Developer Nanodegree program. Your feedback is most welcome. 

## Demo
A working demo of this project can be found over [here](https://sdey96.github.io/udacity-movie-trailer-website/fresh_tomatoes.html).

## Requirements
To run this program, you need to have the latest version of Python 3 installed. It can be downloaded from [here](https://www.python.org/downloads/).

## Project Contents
Within this repository, you'll find the following files:
```
udacity-movie-trailer-website/
├── entertainment_center.py
├── media.py
├── fresh_tomatoes.py
├── fresh_tomatoes.html
├── LICENSE
└── README.md
```
Information about the main Python files:

 1. `entertainment_center.py` - Includes all the instances of the class `Movie` which are basically the movie information. All the instances are passed as a list to `fresh_tomatoes.py` which then generates an HTML Web page containing the list of movies.
2.  `media.py` - Defines the class `Movie`.
3. `fresh_tomatoes.py` - Contains the HTML structure for the website. The main function is `open_movies_page( )` which generates the static HTML Web page by taking instances from the class `Movie` defined in `media.py`.
