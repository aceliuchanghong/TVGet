class Result:
    def __init__(self, name, date, title, poster, mp4name, mp4url, mp4path=None, mp3path=None, srtpath=None,
                 coverpath=None, anspath=None, describe=None):
        self.name = name
        self.date = date
        self.title = title
        self.poster = poster
        self.mp4name = mp4name
        self.mp4url = mp4url
        self.mp4path = mp4path
        self.mp3path = mp3path
        self.srtpath = srtpath
        self.coverpath = coverpath
        self.anspath = anspath
        self.describe = describe

    def __str__(self):
        return f"Name: {self.name}\nDate: {self.date}\nTitle: {self.title}\nPoster: {self.poster}\nMP4 Name: {self.mp4name}\nMP4 URL: {self.mp4url}\nMP4 Path: {self.mp4path}\nMP3 Path: {self.mp3path}\nSRT Path: {self.srtpath}\nCover Path: {self.coverpath}\nAnswer Path: {self.anspath}\nDescribe Path: {self.describe}"
