""" Module for managing and showing information about media content. """


class Movie():
    """ This class is used for storing information about the movies.

    Attributes:
        - movie_title            : Movie title.
        - movie_duration         : Duration of the movie.
        - movie_description      : Description of the movie.
        - movie_genre            : Genre of the movie.
        - movie_release          : Release date of the movie.
        - movie_imdb_ratings     : Main actors inside the movie.
        - poster_image           : URL of movie poster image.
        - trailer_youtube        : URL of movie's YouTube trailer.
    """

    def __init__(self, movie_title, movie_duration, movie_description, 
                 movie_genre, movie_release, movie_imdb_ratings, 
                 poster_image, trailer_youtube): 
        self.release = movie_release
        self.imdb_ratings = movie_imdb_ratings
        self.poster_image_url = poster_image
        self.trailer_youtube_url =  trailer_youtube
        self.genre = movie_genre
        self.description = movie_description
        self.title = movie_title
        self.duration = movie_duration
