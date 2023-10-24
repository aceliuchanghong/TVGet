class Result:
    def __init__(self, name, date, title, poster, mp4name, mp4url):
        self.name = name
        self.date = date
        self.title = title
        self.poster = poster
        self.mp4name = mp4name
        self.mp4url = mp4url

    def __str__(self):
        return f"Name: {self.name}\nDate: {self.date}\nTitle: {self.title}\nPoster: {self.poster}\nMP4 Name: {self.mp4name}\nMP4 URL: {self.mp4url}"


