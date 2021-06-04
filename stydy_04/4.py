from Deque.Deque import Deque

#  回文
def palchecker(asting):
    chardeque = Deque()
    for ch in asting:
        chardeque.addRear(ch)
    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
             stillEqual = False
    return stillEqual


print(palchecker('saas'))