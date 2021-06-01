dict_one = {
    "name": 'zhang',
    "age": 10
}

# len() 返回字典中包含 项 的个数
len(dict_one) # 2
# dict_one['name]
print(dict_one['name'])
# 设置字典中 某一项的值
dict_one['name'] = '杨鹏飞'
# 删除 某一项
del dict_one['name']
# 查询 字典中 是否包含 键为 c 的项
'name' in dict_one  # false
'age' in dict_one # true

dict_two = {
    "a": 1,
    "b": 2,
    "c": 3
}
# 删除健为 "a" 的 一项 返回值为 这一项的 值
# dict_two.pop('b')

# dict_two.popitem()
# dict_two.clear() # 删除字典中全部内容
# a = dict_two.copy()   # 深拷贝
# a["a"] = 4
# dict_two.get("a")  # 获取对应key的值 没有返回 none

dict_two.setdefault('d', 4)
# items keys values
print(dict_two)


