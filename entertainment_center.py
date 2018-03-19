import media
import fresh_tomatoes


# Create instances of class `Movie` - for each movie.

the_terminator = media.Movie("The Terminator",
                             "1 hour 48 minutes",
                             "The story of a cyborg sent past in time.",
                             "Sci-fi, Action",
                             "26 October 1984",
                             "8.0",
                             "https://goo.gl/J8m6ww",
                             "https://youtu.be/c4Jo8QoOTQ4")

avatar = media.Movie("Avatar",
                     "2 hours 42 minutes",
                     "A marine on an alien planet.",
                     "Action, Adventure, Sci-fi, Fantasy",
                     "18 December 2009",
                     "7.8",
                     "https://goo.gl/eTxWYy",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


avengers3 = media.Movie("Avengers: Infinity War",
                        "2 hours 36 minutes",
                        "Avengers assemble to defeat Thanos.",
                        "Sci-fi, Action",
                        "25 April 2018",
                        "8.2",
                        "https://goo.gl/YSEU5c",
                        "https://youtu.be/6ZfuNTqbHE8")

maze_runner2 = media.Movie("Maze Runner 2",
                           "2 hours 13 minutes",
                           "Few selected ones save themselves from "
                           "an organisation called WCKD.",
                           "Sci-Fi, Dystopian, Adventure",
                           "18 September 2015",
                           "6.3",
                           "https://goo.gl/8XtvMQ",
                           "https://youtu.be/SDofO3P2HpE")

thor_ragnarok = media.Movie("Thor Ragnarok",
                            "2 hours 10 minutes",
                            "Thor fights his evil sister, Hela, "
                            "and protects Asgard from her.",
                            "Comedy, Fantasy, Action",
                            "3 November 2017",
                            "8.0",
                            "https://goo.gl/5SkAsT",
                            "https://youtu.be/v7MGUNV8MxU")

justice_league = media.Movie("Justice League",
                             "2 hours",
                             "The Justice League assembles to defeat "
                             "Darkseid.",
                             "Action, Sci-Fi, Fantasy",
                             "15 November 2017",
                             "6.8",
                             "https://goo.gl/x1BpEi",
                             "https://youtu.be/r9-DM9uBtVI")

# Create a list of Movie instances.
movies = [the_terminator, avatar, avengers3, maze_runner2,
          thor_ragnarok, justice_league]

# Generate a Web page by passing the list of Movie instances.
fresh_tomatoes.open_movies_page(movies)
