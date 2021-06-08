from Queue.Queue import Queue
class BiTreeNone:
    def __init__(self, data):
        self.data = data
        self.left_childer = None # 左子树
        self.right_childer = None # 右子树


# 生成节点
a = BiTreeNone('A')
b = BiTreeNone('B')
c = BiTreeNone('C')
d = BiTreeNone('D')
e = BiTreeNone('E')
f = BiTreeNone('F')
g = BiTreeNone('G')

e.left_childer = a
e.right_childer = g
a.right_childer = c
c.left_childer = b
c.right_childer = d
g.right_childer = f


root = e


def pre_order(root): # 前序 遍历
    if root:
        print(root.data, end=',')
        pre_order(root.left_childer)
        pre_order(root.right_childer)


def in_order(root): # 中序 遍历
    if root:
        in_order(root.left_childer)
        print(root.data, end=',')
        in_order(root.right_childer)

def laser_order(root): # 后序 遍历
    if root:
        laser_order(root.left_childer)
        laser_order(root.right_childer)
        print(root.data, end=',')


def leave_order(root): # 层序 遍历
    queue = Queue()
    queue.enqueue(root)
    while queue.size() > 0:
        node = queue.dequeue()
        print(node.data, end=',')
        if node.left_childer:
            queue.enqueue(node.left_childer)
        if node.right_childer:
            queue.enqueue(node.right_childer)




leave_order(root)

