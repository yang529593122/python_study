from Stack.Stack import Stack


# 利用栈来匹配括号 ([{
def par_check(symbolString):
    s = Stack()
    is_mark = True
    index = 0
    while index < len(symbolString) and is_mark:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                is_mark = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    is_mark = False
        index = index + 1
    if is_mark and s.isEmpty():
        return True
    else:
        return False


def matches(top, symbol):
    opens = '([{'
    closer = ')]}'
    return opens.index(top) == closer.index(symbol)


print(par_check('()[]{}'))
print(par_check('{[]()()}'))
print(par_check('({[][][][]})()'))

