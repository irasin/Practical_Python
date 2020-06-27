"""
记录下简单的urllib操作

"""

from urllib import request
# request是向request发送请求的模块
# request.urlopen()
#                 read()
#                 geturl()
#                 getcode()
#                 getheaders()
#                 gethead()  
# request.urlretrieve()



# requese.urlopen(url) 获取响应，返回response对象

base_url = 'http://www.baidu.com'
image_url = 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2117210684,2445859294&fm=26&gp=0.jpg'


response = request.urlopen(url=base_url)

# response对象支持的常用方法

# read()，返回byte类型，需要decode()成string，编码格式依据网页决定
print(response.read().decode('utf-8'))

## example：保存图片
response = request.urlopen(url=image_url)

# 由于是保存图片，所有直接read成byte类型保存即可
with open('github.jpg', 'wb') as f:
    f.write(response.read())


# geturl()，返回请求的url的string
print(response.geturl())

# getcode()，返回状态码，200为正常访问
print(response.getcode())

# getheaders()，返回所有header信息的list，每个健值对保存为一个二元tuple，存放在list中
print(response.getheaders())

# getheader(key)，返回header信息中某个key对应的值，string格式
print(response.getheader('Server'))


###############################################################################

# request.urlretrieve(url, file_name) 可直接保存url响应内容，返回保存的路径名与head信息
a, b = request.urlretrieve(url=image_url, filename='github2.jpg')


################################################################################

from urllib import parse
# parse是关于编解码url的模块
# parse.quote()
# parse.unquote()
# parse.urlencode()


# url只支持特定字符，数字，字母，下划线，出现其他的需要进行编码 -》 就是平常看到的各种百分号
# 同样，我们解读url的时候，需要解码才能识别相应的内容

# parse.quote()，url编码，将指定字符转换为%XXX
url1 = 'https://www.baidu.com/s?ie=UTF-8&wd=百度'
url1_encoded = parse.quote(url1)
print(url1_encoded) 
# https%3A//www.baidu.com/s%3Fie%3DUTF-8%26wd%3D%E7%99%BE%E5%BA%A6


# parse.unquote()，url解码，将%XXX转换为指定字符
url1_decoded = parse.unquote(url1_encoded)
print(url1_decoded)
# https://www.baidu.com/s?ie=UTF-8&wd=百度

# parse.urlencode(dict)，将dict中的健值对自动quote然后拼接成url的query_string格式
data = {'ie': 'utf-8', 'wd': '百度', 'target': 'github'}
data_encoded = parse.urlencode(data)
print(data_encoded)

# 等价于以下操作
res = []
for k, v in data.items():
    res.append(f'{parse.quote(k)}={parse.quote(v)}')
res = '&'.join(res)
print(res)
print(res == data_encoded)


#####################################################################################
from urllib import request


# request.Request()，构建请求对象，模拟浏览器登陆
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

req = request.Request(url=base_url, headers=headers)

response = request.urlopen(req)
print(response.read().decode())

####################################################################################
# get: query在url后拼接
# post:

# post方式范例


post_url = 'https://fanyi.baidu.com/sug'

word = 'eng'
form_data = {'kw': word}
form_data = parse.urlencode(form_data).encode()
req = request.Request(url=post_url, headers=headers)

response = request.urlopen(req, data=form_data)

import json
res = json.dumps(json.loads(response.read().decode()),ensure_ascii=False, indent=2)
print(res)


# 或者
word = 'eng'
post_url = 'https://fanyi.baidu.com/sug'
form_data = {'kw': word}
form_data = parse.urlencode(form_data).encode()
req = request.Request(url=post_url, data=form_data, headers=headers, method='POST')
response = request.urlopen(req)

res = json.dumps(json.loads(response.read().decode()),
                 ensure_ascii=False, indent=2)
print(res)
