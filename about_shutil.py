"""
记录一下python中shutil的一些操作
"""
import shutil

shutil.copy('src', 'dst') # 单一文件copy或者copy到某一目录下,dst可为文件或者目录
shutil.copy2('src', 'dst') # shutil.copy加上shutil.copystat
shutil.copyfile('src', 'dst') # 单一文件copy，dst必须为文件
shutil.copyfileobj(open('src', 'r'), open('dst', 'w')) # copy文件内容
shutil.copymode('src', 'dst') # 权限copy
shutil.copystat('src', 'dst') # 状态copy

shutil.move('src', 'dst') # 移动或者重命名文件



shutil.copytree('src', 'dst') # 目录整体copy
shutil.rmtree('path') # 目录整体强制删除

shutil.make_archive('src', 'formart:{zip or tar or other}', 'dst_dir') # 指定格式压缩文件到某一目录
shutil.get_archive_formats() # 获取当前系统支持的压缩format，对应上一个中的format

shutil.unpack_archive('src', 'dst_dir') # 解压缩文件到某一目录，format会采取文件后缀名
shutil.get_unpack_formats()  # 获取当前系统支持的解压缩format
