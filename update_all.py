import os
import time
from datetime import datetime

# 设置要更改的目录路径和新的修改日期
directory_path = r'C:\Users\86135\Desktop\数字逻辑\数字逻辑实验\实验三\1320221095 徐帅'
new_modification_time = datetime(2024, 6, 10, 14, 26, 0)  # 设置新的修改日期和时间

# 将datetime对象转换为时间戳
new_modification_timestamp = new_modification_time.timestamp()

# 遍历目录及其子目录中的所有文件和文件夹
for root, dirs, files in os.walk(directory_path):
    for filename in files:
        file_path = os.path.join(root, filename)

        # 更改文件的修改时间
        os.utime(file_path, (new_modification_timestamp, new_modification_timestamp))

    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)

        # 更改文件夹的修改时间
        os.utime(dir_path, (new_modification_timestamp, new_modification_timestamp))

print("文件及文件夹的修改日期已更新。")
