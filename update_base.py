import os
import time
from datetime import datetime

# 设置要更改的目录路径和新的修改日期
directory_path = '你的地址'
new_modification_time = datetime(2024, 6, 9, 15, 34, 0)  # 设置新的修改日期和时间

# 将datetime对象转换为时间戳
new_modification_timestamp = new_modification_time.timestamp()

# 遍历目录中的所有文件
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)

    # 检查是否是文件
    if os.path.isfile(file_path):
        # 更改文件的修改时间
        os.utime(file_path, (new_modification_timestamp, new_modification_timestamp))

print("文件修改日期已更新。")
