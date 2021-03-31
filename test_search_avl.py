import time
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from blackfire import probe

from utils.bst import BST


## Measuring insert time, random data, AVL vs BST

np.random.seed(0)
N_DATA = 500_000
rand_data = np.random.randint(-100000, 100000, (N_DATA, ))
ordered_data = np.arange(0, N_DATA)
slices = [5, 10, 50, 100, 500, 1_000, 5_000, 10_000, 50_000, 100_000, 500_000, 1_000_000, 5_000_000, 10_000_000]
times_insert_avl = {s: [] for s in slices}
times_insert_bst = {s: [] for s in slices}
times_insert_bst_worst = {s: [] for s in slices}

avl = BST(avl=True)
for idx, d in enumerate(rand_data):
    avl.insert(d)



## Measuring search time, AVL vs BST

probe.initialize(title='search_avl_500k')
probe.enable()
probe.add_marker(f'Profile AVL search')
t = time.time()
for idx, d in enumerate(rand_data):
    avl.find(d)
    if (idx + 1) in slices:
        probe.add_marker(f'{(idx + 1)}th point found in AVL')

probe.disable()
probe.end()
