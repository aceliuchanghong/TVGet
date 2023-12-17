from datetime import datetime

def get_current_hour():
    now = datetime.now()
    print(datetime.now().hour)
    return now.hour

# 使用函数
current_hour = get_current_hour()
print(current_hour)
