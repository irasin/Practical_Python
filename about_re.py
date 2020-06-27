"""
记录下正则表达式re的一些操作
https://www.runoob.com/python/python-reg-expressions.html
https://c.runoob.com/front-end/854
"""

import re

# .     表示除 "\n"外任意单个字符
# [ ]   字符集合，表示括号内任意单个字符
# [^ ]  非字符集合，表示非括号内字符的任意单个字符
# *     表示前一个字符0次以上出现
# +     表示前一个字符1次以上出现
# ?     表示前一个字符0次或1次
# |     表示左右表达式任意一个
# {m}   表示前一个字符出现m次
# {m, n}表示前一个字符出现m到n次（包含m与n）
# ^     表示字符串开头
# $     表示字符串结尾
# ()    分组标记，表示一个整体，同时内部可用|分割不同表达式
# \d  　表示所有数字，相当于[0-9]
# \w    表示所有数字字母与下划线，相当于[A-Za-z0-9_]


# 一般会创建匹配的pattern，同时建议pattern前加上r，取消转义
# 简单的匹配也可以不用创建pattern，直接匹配
# re.compile(pattern, flags) flga也可在re的各个方法中指定
# 多个flag可以通过 | 来同属输入指定

# flags: 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
# re.I 忽略大小写
# re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
# re.M 多行模式
# re.S 使 . 包括换行符在内的任意字符（原本 . 不包括换行符）
# re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于Unicode字符属性数据库
# re.X 为了增加可读性，忽略空格和#后面的注释

pattern = re.compile(r'AA')

# re.match(pattern, string) 从string的开头匹配pattern，若成功则返回match对象
re.match('aa', 'aaAdsaasaa')  # <re.Match object; span=(0, 2), match='aa'>

# re.search(pattern, string) 检测string中是否含有pattern，若存在则返回第一处匹配到的match对象
re.search('aa', 'Adsaasaa') ## <re.Match object; span=(3, 5), match='aa'>

# re.findall(pattern, string) 返回string中所有的满足pattern的字符串的list
re.findall('aa', 'Adsaasaa')  # ['aa', 'aa']

# re.split(pattern, string) 将string按照pattern进行分割，返回分割后的list
re.split('aa', 'Adsaasaa')  # ['Ads', 's', '']

# re.finditer(pattern, string) findall的iterator版本，每次返回一个match对象
for i in re.finditer('aa', 'Adsaasaa'):
    print(i)
## <re.Match object; span=(3, 5), match='aa'>
## <re.Match object; span=(6, 8), match='aa'>

# re.sub(pattern, replace, string) 将string中pattern的部分替换为replace，返回字符串
# count指定替换次数，默认为0，表示全部
# replace也可为一个函数，对pattern部分进行处理
re.sub('aa', 'AA', 'Adsaasaa', count=0)  # 'AdsAAsAA'


####################
# match对象支持的方法
# start()   返回开始的index
# end()     返回结尾的下一位的index
# span()    返回(start, end)的tuple
# group()   返回匹配到的对象
# 若匹配对象为包含空格的长字符串，span()和group()通过输入index作为参数获得子串的信息

