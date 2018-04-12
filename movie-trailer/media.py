import webbrowser


# parent class
class Video():
    # VALID_RATINGS = ["G", "PG", "PG13", "R"]

    def __init__(self, video_title, video_duration, video_poster_image,
                 video_trailer_youtube):
        self.title = video_title
        self.duration = video_duration
        self.poster_image_url = video_poster_image
        self.trailer_youtube_url = video_trailer_youtube


# child class of Video
class Movie(Video):
    def __init__(self, movie_title, movie_duration, movie_poster_image_url,
                 movie_trailer, movie_storyline, movie_year):
        Video.__init__(self, movie_title, movie_duration,
                       movie_poster_image_url, movie_trailer)
        self.storyline = movie_storyline
        self.year_release = movie_year

    def show_trailer(self):
        webbrowser.open(self.movie_trailer)


# child class of Video
class TV_Shows(Video):
    def __init__(self, show_title, show_season, show_poster_image,
                 show_trailer_youtube, show_episodes, show_tv_station):
        Video.__init__(self, show_title, show_season, show_poster_image,
                       show_trailer_youtube)
        self.episodes = show_episodes
        self.tv_station = show_tv_station

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
