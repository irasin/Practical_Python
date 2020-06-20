"""
记录一下os模块中的一些操作
"""

import os

# OS中的一些常用变量
os.sep # 路径分隔符，Linux中为/，Windows中为\\（第一个为转义字符）
os.extsep # 拓展名分隔符，在各个平台都是统一的. 
os.name # 操作系统名，Linux中为posix，Windows中为nt
os.pathsep # PATH中的环境变量分隔符，Linux中为:，Windows中为;
os.environ # 系统环境变量，格式为dict
os.curdir # 当前目录 .
os.pardir # 上级目录 ..


# OS中关于dir的一些操作
os.getcwd() # 获取当前工作目录的绝对路径
os.chdir('dirname') # 变更工作目录

os.mkdir('dirname') # 生成单个目录
os.rmdir('dirname') # 删除单个目录

os.makedirs('dir1/dir2') # 从前往后递归生成目录
os.removedirs('dir1/dir2') # 从后往前递归删除目录，直至遇到非空目录

os.listdir('dirname') # 返回一个list 列出指定目录下所有目录与文件，包括被隐藏的
os.walk('dirname') # 返回一个生成器，以（dirpath, dirnames, filenames)的形式递归遍历

os.remove('filename') # 删除一个文件

os.rename('filename or dirname') # 重命名文件或目录
os.stat('filename or dirname') # 返回一个dict, 显示文件或目录的信息


# os.path模块中常用的一些操作
os.path.abspath('path') # 返回path的绝对路径
os.path.dirname('path') # 返回path的目录，等价于os.path.split('path')[0]
os.path.basename('path') # 返回path最后的文件名，等价于os.path.split('path')[1]

os.path.split('path')  # 返回一个tuple，分割目录与文件名
os.path.splitext('path')  # 返回一个tuple，分割文件路径与文件拓展名

os.path.join('path1', 'path2', 'path3')  # 组合各个path

os.path.exists('path') # 判断path是否存在
os.path.isabs('path')  # 判断path是否为绝对路径
os.path.isdir('path')  # 判断path是否为目录
os.path.isfile('path')  # 判断path是否为文件

os.path.getsize('path') # 返回大小（字节）
os.path.getctime('path') # 返回创建时间戳(浮点数)
os.path.getmtime('path') # 返回最近修改时间戳
os.path.getatime('path')  # 返回最近访问时间戳

os.path.normcase('path') # Windows上用，将path中所有字符小写，并把斜杠换成反斜杠
os.path.normpath('path') # 返回去除冗余的路径

os.path.samefile('path1', 'path2') # 判断是否指向同一路径
os.path.sameopenfile('fp1', 'fp2') # 判断是否指向同下文件


###########
# 常用的操作
###########

# 1.创建日志文件夹
if not os.path.exists('result'):
    os.mkdir('result1')
    os.makedirs('result2/result3')
    
# 或者用try
try:
    os.mkdir('result1')
except FileExistsError:
    ...
    

# 2.在指定目录中搜寻文件
path = 'path'
target_name = 'filename.txt'
for root, dirs, files in os.walk(path):
    for name in files:
        if name in files:
            print(os.path.join(root, name))


# 用glob最好
from glob import glob
for file in glob(f'{path}*{target_name}'):
    print(file)
