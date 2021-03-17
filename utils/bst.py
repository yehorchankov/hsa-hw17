class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
        return f'<{self.data}>'


class BST:
    root = None

    def __init__(self, avl=False):
        self.avl = avl

    def insert(self, data):
        self.root = self._insert(data, self.root)

    def _insert(self, data, node):
        if node is None:
            return Node(data)
        elif data < node.data:
            node.left = self._insert(data, node.left)
        else:
            node.right = self._insert(data, node.right)

        if not self.avl:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        if balance > 1 and data < node.left.data:
            return self.rotate_right(node)
        elif balance < -1 and data > node.right.data:
            return self.rotate_left(node)
        elif balance > 1 and data > node.left.data:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        elif balance < -1 and data < node.right.data:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def delete(self, data):
        self.root = self._delete(data, self.root)

    def _delete(self, data, node):
        if node is None:
            print('Data not found')
            return node

        if data < node.data:
            node.left = self._delete(data, node.left)
        elif data > node.data:
            node.right = self._delete(data, node.right)
        else:
            if node.left and node.right:
                node.data = self._find_max(node.left.data, node.left)
                node.left = self._delete(node.data, node.left)
            elif node.left:
                node = node.left
            elif node.right:
                node = node.right
            else:
                return None

        if not self.avl:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        elif balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)
        elif balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        elif balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def _find_max(self, value, node):
        if node is None:
            return value
        else:
            return self._find_max(node.data, node.right)

    def find(self, data):
        node = self._find(data, self.root)
        # print(node)

    def _find(self, data, node):
        if node is None:
            return node
        if data == node.data:
            return node
        elif data < node.data:
            return self._find(data, node.left)
        elif data > node.data:
            return self._find(data, node.right)

    def get_height(self, node):
        if node is None:
            return 0

        return node.height

    def get_balance(self, node):
        if node is None:
            return 0

        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, node):
        if node.right is None:
            return node
        new_root = node.right
        left = new_root.left
        new_root.left = node
        node.right = left
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def rotate_right(self, node):
        if node.left is None:
            return node
        new_root = node.left
        right = new_root.right
        new_root.right = node
        node.left = right
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def order_traverse(self):
        if self.root is not None:
            self._traverse(self.root)
            print('\n')
        else:
            print('Empty')

    def _traverse(self, node):
        if node.left is not None:
            self._traverse(node.left)
        print(node.data, end=' ')
        if node.right is not None:
            self._traverse(node.right)

    def get_tree_height(self):
        if self.root is None:
            return 1
        return self._height(self.root, 0)

    def _height(self, node, h):
        if node is None:
            return h

        if node.left is None and node.right is None:
            return h + 1

        left_h = self._height(node.left, 0)
        right_h = self._height(node.right, 0)
        return h + max(left_h, right_h) + 1
