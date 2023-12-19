class PicResult:
    def __init__(self):
        self.name = None  # 文件名字
        self.ext = None  # 后缀
        self.date = None  # 日期
        self.keyword = None  # 关键字
        self.url = None  # 链接地址
        self.downpath = None  # 下载路径
        self.bakpath = None  # 备份路径
        self.fix1path = None  #
        self.fix2path = None  #
        self.fix3path = None  #
        self.fix4path = None  #
        self.fix5path = None  #
        self.fix6path = None  #
        self.fix7path = None  #
        self.fix8path = None  #
        self.fix9path = None  #
        self.fix10path = None  #
        self.fix11path = None  #
        self.fix12path = None  #
        self.anspath = None  # 结果路径
        self.describe = None  # 备注

    def __str__(self):
        attrs = ['name', 'ext', 'date', 'keyword', 'url', 'downpath', 'bakpath',
                 'fix1path', 'fix2path', 'fix3path', 'fix4path', 'fix5path',
                 'fix6path', 'fix7path', 'fix8path', 'fix9path', 'fix10path', 'fix11path',
                 'fix12path', 'anspath', 'describe']
        return '\n'.join(f'{attr}="{getattr(self, attr)}"' for attr in attrs)

    def to_clazz(self):
        attrs = ['name', 'ext', 'date', 'keyword', 'url', 'downpath', 'bakpath',
                 'fix1path', 'fix2path', 'fix3path', 'fix4path', 'fix5path',
                 'fix6path', 'fix7path', 'fix8path', 'fix9path', 'fix10path', 'fix11path',
                 'fix12path', 'anspath', 'describe']
        return '\n'.join(f'picresult.{attr} = "{getattr(self, attr)}"' for attr in attrs)


class PicInfo:
    def __init__(self):
        self.name = None
        self.ext = None
        self.width = 0
        self.height = 0

    def __str__(self):
        return f'\n{self.name}.{self.ext}:Width={self.width}, Height={self.height}'
