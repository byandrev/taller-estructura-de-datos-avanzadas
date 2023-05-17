from Print import print_tree
import random
from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)
    

def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root


def generate_random_tree(nodes, is_completed):
    if nodes == 0:
        return None

    root = TreeNode(random.randint(1, 100))
    nodes -= 1

    queue = deque([root])

    while nodes > 0:
        b = random.randint(0, 2)
        node = queue.popleft()

        if nodes > 0:
            left_val = random.randint(1, 100)
            node.left = TreeNode(left_val)
            queue.append(node.left)
            nodes -= 1

        if nodes > 0:
            right_val = random.randint(1, 100)
            node.right = TreeNode(right_val)
            queue.append(node.right)
            nodes -= 1


    return root


def level_order_traversal(root, ans):
    height = get_height(root)
    for level in range(1, height + 1):
        print_level(root, level, ans)

def get_height(node):
    if node is None:
        return 0
    else:
        height_left = get_height(node.left)
        height_right = get_height(node.right)
        return max(height_left, height_right) + 1

def print_level(node, level, ans):
    if node is None:
        ans.append("null")
        return
    if level == 1:
        ans.append(node.val)
    elif level > 1:
        print_level(node.left, level - 1, ans)
        print_level(node.right, level - 1, ans)



# Recibe como parametro True o False si el arbol es completo o no
# return a list, Example: [1,2,null]
def generate(is_completed=False):
    # 1 to 30 nodes
    n = random.randint(1, 30)
    tree = None
    
    if is_completed==False: tree = generate_random_tree(n, False)
    else: tree = generate_random_tree(n, True)

    print(print_tree(tree))

    if tree:
        tree_ans = []
        level_order_traversal(tree, tree_ans)
        ans = str(tree_ans).replace(" ", "").replace("'null'", "null")
        print(ans)
        return ans
    else:
        return "[]"
