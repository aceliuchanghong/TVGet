class PicResult:
    def __init__(self):
        self.name = None  # 名字
        self.ext = None  # 后缀
        self.date = None  # 日期
        self.keyword = None  # 关键字
        self.url = None  # 链接地址
        self.downpath = None  # 下载路径
        self.bakpath = None  # 备份路径
        self.fix1path = None  # 1处理之后路径
        self.fix2path = None  # 2处理之后路径
        self.fix3path = None  # 3处理之后路径
        self.anspath = None  # 结果路径
        self.describe = None  # 备注

    def __str__(self):
        return f'\nname(名字)="{self.name}",\n' \
               f'ext(后缀)="{self.ext}",\n' \
               f'date(日期)="{self.date}",\n' \
               f'keyword(关键字)="{self.keyword}",\n' \
               f'url(链接地址)="{self.url}",\n' \
               f'downpath(下载路径)="{self.downpath}",\n' \
               f'bakpath(备份路径)="{self.bakpath}",\n' \
               f'fix1path(1处理之后路径)="{self.fix1path}",\n' \
               f'fix2path(2处理之后路径)="{self.fix2path}",\n' \
               f'fix3path(3处理之后路径)="{self.fix3path}",\n' \
               f'anspath(结果路径)="{self.anspath}",\n' \
               f'describe(备注)="{self.describe}"'


class PicInfo:
    def __init__(self):
        self.name = None
        self.ext = None
        self.width = 0
        self.height = 0

    def __str__(self):
        return f'\n{self.name}.{self.ext}:Width={self.width}, Height={self.height}'
