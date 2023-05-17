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