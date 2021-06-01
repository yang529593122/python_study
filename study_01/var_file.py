# 全局变量 局部变量

# 局部变量
# 在函数内部定义的变量 只能在函数内部使用 在函数外部不能使用
# def show():
#     score = 100
#     print('分数', score)
#
#
# show()
# # print(score)  # 报错 not defined


# 全局变量
# 在函数外部定义的变量

# a = 100
#
#
# def one():
#     a = 200
#     print(a)
#
#
# def two():
#     print(a)
#
#
# one()
# two()


# 函数内部如何改变全局变量
a = 200


def chang():
    global a
    a = 100
    print(a)


chang()
print(a)






