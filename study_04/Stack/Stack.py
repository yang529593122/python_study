# 数据结构 栈

# 先进后出
# is_empty 判断 栈 是否为空
# push 进栈
# pop  出栈
# peek 查看栈顶 元素
# size 查看栈的长度


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
