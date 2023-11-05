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
        return f'name="{self.name}",\n' \
               f'date="{self.date}",\n' \
               f'title="{self.title}",\n' \
               f'poster="{self.poster}",\n' \
               f'mp4name="{self.mp4name}",\n' \
               f'mp4url="{self.mp4url}",\n' \
               f'mp4path="{self.mp4path}",\n' \
               f'mp3path="{self.mp3path}",\n' \
               f'srtpath="{self.srtpath}",\n' \
               f'coverpath="{self.coverpath}",\n' \
               f'anspath="{self.anspath}",\n' \
               f'describe="{self.describe}"'
