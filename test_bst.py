import numpy as np

from utils.bst import BST

np.random.seed(42)
ints = np.random.randint(-10000000, 10000000, (2**15, ))
print(ints)
avl = BST(avl=False)

for i in ints:
    avl.insert(i)

# avl.order_traverse()

print(avl.get_tree_height())
print(avl.root.height)
avl.delete(71)

# avl.order_traverse()

print(np.log2(len(ints)))
