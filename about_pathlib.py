"""
简介
它是python3.4新增的一个标准库，提供文件路径相关的操作方式
操作涉及：查 → 增 → 删 → 改
查
from pathlib import Path
​
cwd_path = Path.cwd()            # 获取当前工作路径
file_path = Path(__file__)       # 针对当前文件构建一个路径对象-WindowsPath
file_path.parent                 # 获取上级路径
file_path.joinpath(str)          # 获取子路径   等价于   file_path / str
file_path.glob(filename)         # 返回路径下所有符合filename格式(例如‘*.txt'的文件，返回迭代器
file_path.rglob(filename)        # 与glob类似，但是它返回所有子文件夹的符合filename的文件
file_path.iterdir()         # 当path为文件夹时，通过yield产生path文件夹下的所有文件、路径的迭代器
​
file_path.name                   # 获取path的文件名
file_path.suffix                 # 获取文件后缀
file_path.stem                   # 文件名不带后缀
​
file_path.is_dir()               # 是否为文件夹
file_path.is_file()              # 是否为文件
增
P = Path(file)
​
P.mkdir(parents=True, exist_ok=True)    # 创建文件夹，当parents为True时依次创建路径中间缺少的文件夹
​
删
P.rmdir()                 # 当路径为空文件夹的时候，删除该文件夹
                          # 使用os模块进行删动作
os.rmdir()                # 等价与P.rmdir()
os.remove(P)           # 删除文件路径，如果这个路径是一个文件夹，则抛出osError异常
                
改
P.rename(target)          # 当target为str时，重命名文件或文件夹，当target是Path时，重命名并移动文件
P.replace(target)         # 重命名当前文件或文件夹，如果target所指示的文件已存在，则覆盖原文件
​
# *** 修改当前路径
import os 
os.chdir(dir)
"""


import pathlib
from pathlib import Path

cwd_path = Path.cwd()            # 获取当前工作路径
# file_path = Path(__file__)       # 针对当前文件构建一个路径对象-WindowsPath
cwd_path.parent                 # 获取上级路径
cwd_path.joinpath(str)         # 获取子路径   等价于   file_path / str
filename = "*py"
g1 = cwd_path.glob(filename)         # 返回路径下所有符合filename格式(例如‘*.txt'的文件，返回迭代器
g2 = cwd_path.rglob(filename)        # 与glob类似，但是它范围所有子文件夹的符合filename的文件
g3 = cwd_path.iterdir()         # 当path为文件夹时，通过yield产生path文件夹下的所有文件、路径的迭代器
​
for i in g1:
    print(i)

for i in g2:
    print(i)

for i in g3:
    print(i)
