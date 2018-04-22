# Movie Trailer Website
## About
The Movie Trailer Website project consists of server-side code to store a list of movies titles, along with its respective box art imagery, and other information about them. The data is served as an HTML Web page allowing visitors to review the movies and watch the trailers.

This project is being created as part of Udacity's [Full-Stack Web Developer Nanodegree](https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004) program. Your feedback about this project is most welcome. 

## Demo
A working demo of this project can be found over [here](https://sdey96.github.io/udacity-movie-trailer-website/fresh_tomatoes.html).

## Requirements
To run this program, you must have the following applications installed:
1. The latest version of Python 3. It can be downloaded from [here](https://www.python.org/downloads/).
2. [Optional] Git. It can be downloaded from [here](https://git-scm.com/downloads).

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
**Information about above Python files:**

 1. `entertainment_center.py` - Includes all the instances of the class `Movie` which basically define the movie information. Each instance defines the information of one movie. All the instances are passed as a list to the file`fresh_tomatoes.py` through the function `open_movies_page()` which generates an HTML Web page containing the list of movies along with their information.
2.  `media.py` - Defines the class `Movie`.
3. `fresh_tomatoes.py` - Defines the HTML structure for the website. The principal function is `open_movies_page()` which generates a static HTML Web page by taking a list instances of the class `Movie` defined in `media.py`.

## Steps to run this project

 1. Install the latest version of Python 3 from [here](https://www.python.org/downloads/) if not already installed.
 2. [Optional] Install Git from [here](https://git-scm.com/downloads). If you have downloaded the project manually, skip to step 4. Otherwise, follow the next step.
 3. Open terminal, and clone this repository by typing the following command:
 
 ```bash
   git clone https://github.com/SDey96/udacity-movie-trailer-website.git
```

 4. Navigate to the directory `udacity-movie-trailer-website/`.
 5. Open a terminal in the aforementioned directory and type the following command:
 
   If you are using Windows, then type 
    ```powershell 
         python.exe .\entertainment_center.py
    ```
        
      (Make sure first that Python is added to PATH.)
  
       If you are using Linux, then type 
         
         python3 entertainment_center.py
  
  6. A Web page will open in your default browser with the list of your favourite movies. Enjoy!

## Support and Contact Info
For any queries or kudos, you may reach out to me on [Twitter](https://twitter.com/SDey_96).

If you are facing any trouble(s) with this project, you may create a new issue [here](https://github.com/SDey96/udacity-movie-trailer-website/issues). 
