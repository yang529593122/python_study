from Node.Node import Node


# 无序链表
class Unorderlist:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = None(item)
        temp.setNext = (self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count+1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext)



mylist = Unorderlist()

print(mylist.head)