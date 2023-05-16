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


def generate_random_tree(nodes):
    if nodes == 0:
        return None

    root = TreeNode(random.randint(1, 100))
    nodes -= 1

    queue = deque([root])

    while nodes > 0:
        b = random.randint(0, 2)
        node = queue.popleft()

        if b==0:
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

        if b==1 and nodes > 0:
            left_val = random.randint(1, 100)
            node.left = TreeNode(left_val)
            queue.append(node.left)
            nodes -= 1

        if b==2 and nodes > 0:
            right_val = random.randint(1, 100)
            node.right = TreeNode(right_val)
            queue.append(node.right)
            nodes -= 1

    return root

def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            result.append(node.val)

            if node.left:
                queue.append(node.left)
            else:
                result.append("null")

            if node.right:
                queue.append(node.right)
            else:
                result.append("null")

    return result



# return a list, Example: [1,2,null]
def generate():
    # 1 to 30 nodes
    n = random.randint(1, 30)
    tree = generate_random_tree(n)
    ans = str(level_order_traversal(tree)).replace(" ", "").replace("'null'", "null")
    return ans


if __name__ == '__main__':
    print(generate_random_tree())