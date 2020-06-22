"""
记录一下pickle与json的一些操作  

serialization 序列化 
unserialization 反序列化 


pickle与json共通的特点
都具有dumps/dump, loads/load方法
其中带s的是实时转换，不写入或读取文件，不带s的则是写入或读取文件用


不同之处主要在于，pickle是转换为字节数据，json是转换为字符数据
"""


import pickle # pickle基本只在python使用

a = 1


a1 = pickle.dumps(a) # 转换为二进制文件格式
print(a1) # b'\x80\x03K\x01.'
a2 = pickle.loads(a1) # 二进制文件转换为源数据
print(a2) # 1

with open('data.pkl', 'wb') as f:
    pickle.dump(a, f)  # 源数据写入为二进制格式文件
       

with open('data.pkl', 'rb') as f:
    b = pickle.load(f) # 二进制格式文件读取成源数据
print(b) # 1




"""
json中{}为基本对象，[]为列表，数据格式与python存在对应关系，如true/false/null
"""
import json # json则是一种通用的格式

data = {'person': [{'name': 'cc', 'age': 25, 'is_valid': True, 'number': 1},
        {'name': 'ira', 'age': 18, 'number': 2, 'is_valid':False, 'number': None}]}

data_json = json.dumps(data, indent=2) # 将python对象转换为json格式
print(data_json) # json为string
# {
#     "person": [
#         {
#             "name": "cc",
#             "age": 25,
#             "is_valid": true,
#             "number": 1
#         },
#         {
#             "name": "ira",
#             "age": 18,
#             "number": null,
#             "is_valid": false
#         }
#     ]
# }
print(type(data_json)) # <class 'str' >

data_1 = json.loads(data_json) # 将json格式转换为python对象
print(data_1) 
# {'person': [{'name': 'cc', 'age': 25, 'is_valid': True, 'number': 1}, {
#     'name': 'ira', 'age': 18, 'number': None, 'is_valid': False}]}
print(type(data_1))  # <class 'dict'>

with open('data.json', 'w') as f: # 源数据写入为json文件
    json.dump(data, f, indent=2)
    
with open('data.json', 'r') as f: # json文件读取成源数据
    data_2 = json.load(f)

print(data_2 == data_1) # True


