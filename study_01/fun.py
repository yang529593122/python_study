# def 函数名:
#     函数体
# 函数名()

# 函数必须先定义才能使用

# 默认参数
def one(name, sex, age=16, city='北京'):
    print(name, sex, age, city)


# one('bod', '男', 10)
#
# one('sd', 'girl', city='上海')

# 可变参数

def two(*arg):
    print(arg)


two(1, 2, 3)
a = [1, 2, 3, 4]
b = (1, 2, 3, 4)
c = {
    "a": 1,
    "b": 2
}
two(*a)
two(*b)
two(c)


# 关键字 参数

# def 函数名（ 参数，参数，**关键字）：
#     函数体
# 函数名（参数，参数，键='值'）

def start(name, age, **kwargs):
    print(name, age, kwargs)


start('yang', 23, sex='boy', hight=178)

kw = {
    'sex': 'boy',
    'height': 176
}
start('yang', 23, **kw)


# 函数返回值
# 函数体中 没有 return    函数的返回值是 none
# 函数体中 返回多个值 用逗号 分隔  返回值的类型是一个元组  例如： return 字符串，数值，列表，元组，字典 。。。。。

