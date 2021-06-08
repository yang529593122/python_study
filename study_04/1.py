from Stack.Stack import Stack

# 利用栈来匹配括号
def par_check(symbolString):
    s = Stack()
    is_mark = True
    index = 0
    while index < len(symbolString) and is_mark:
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                is_mark = False
            else:
                s.pop()
        index = index + 1
    if is_mark and s.isEmpty():
        return True
    else:
        return False


print(par_check('((()))'))
print(par_check('((())'))
print(par_check('()()()'))
print(par_check('()(()'))

