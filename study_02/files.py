# 文件操作

# r 只读
# w 只写 在原文件写，覆盖之前的内容
# a 只写 不复发你原来的内容 末尾追加
# wb 写入 以二进制形式写入 ， 保存图片时使用
# r+ 读写 不覆盖原文件 末尾追加
# w+ 读写 在原文件写 覆盖之前内容
# a+ 读写 不覆盖原文件内容 末尾追加

# 读文件
# f = open(r"test.txt", 'r', encoding='utf-8')
# res = f.read()
# f.close()
# print(res)

# 读文件
# with open(r'test.txt', 'r', encoding='utf-8') as f :
#     res = f.read()
#
# print(res)

# with open(r'test.txt', 'r', encoding='utf-8') as f:
#     for line in f.readlines():
#         print(line.strip())

# 写文件
# with open(r"test.txt", 'a', encoding='utf-8') as f:
#     f.write('下雨了')



