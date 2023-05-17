import collections
from basic import TreeNode, deserialize, level_order_traversal

class CBTInsert(object):
    def __init__(self, root):
        self.deque = collections.deque()
        self.root = root
        q = collections.deque([root])

        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, v):
        node = self.deque[0]
        self.deque.append(TreeNode(v))
        if not node.left:
            node.left = self.deque[-1]
        else:
            node.right = self.deque[-1]
            self.deque.popleft()
        return node.val

    def get_root(self):
        return self.root
    

n = int(input())

for i in range(n):
    tree = input()
    val = int(input())
    tree_node = deserialize(tree)
    obj = CBTInsert(tree_node)
    obj.insert(val)

    tree_ans_list = []
    level_order_traversal(obj.get_root(), tree_ans_list)
    print(tree_ans_list)