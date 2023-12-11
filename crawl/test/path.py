from datetime import datetime

# 获取当前日期和时间
now = datetime.now()

# 格式化日期为 'yyyymmdd' 格式
date_str = now.strftime("%Y%m%d")
print(date_str)
