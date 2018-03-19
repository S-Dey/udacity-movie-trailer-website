"""Module for managing and showing information about media content."""


class Movie():
    """This class stores information about the movies.

    Attributes:
        - title (str)               : Movie title.
        - duration (str)            : Duration of the movie.
        - description (str)         : Description of the movie.
        - genre (str)               : Genre of the movie.
        - release (str)             : Release date of the movie.
        - imdb_ratings (str)        : Main actors inside the movie.
        - poster_image_url (str)    : URL of movie poster image.
        - trailer_youtube_url (str) : URL of movie's YouTube trailer.
    """

    def __init__(self, movie_title, movie_duration, movie_description,
                 movie_genre, movie_release, movie_imdb_ratings,
                 poster_image, trailer_youtube):
        self.release = movie_release
        self.imdb_ratings = movie_imdb_ratings
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.genre = movie_genre
        self.description = movie_description
        self.title = movie_title
        self.duration = movie_duration
