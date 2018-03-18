""" Module for managing and showing information about media content. """


class Movie():
    """ This class is used for storing information about the movies.

    Attributes:
        - movie_release(str):     Release date.
        - movie_main_actors(str): Main actors inside the movie.
        - poster_image(str):      Urof the video poster image.
        - trailer_youtube(str):   Url of the youtube trailer.
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
