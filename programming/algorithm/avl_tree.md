---
title: AVL Tree
---

## AVL Tree
AVL Tree is a self-balancing binary search tree


Balance factor := height of left sub tree - height of righ sub tree

- Insert
    - $O(\log n)$,
- Delete
    - $O(\log n)$,
- Search
    - $O(\log n)$,


## Fundamental operation
Fact

- right node can be parent

Right rotate

Left rotate

```
  r
  |
  a
|   |
b   c
    | |
    d e
```

- (1) If `c` has a left subtree, assign `x` as the parent of the left subtree of `d`.
- (2)
    - If the parent of `a` is NULL, make `c` as the root of the tree.
    - Else if `a` is the left child of `r`, make `c` as the left child of `r`.
    - Else assign `c` as the right child of `r`.
- (3) Change the parent of `a` to that of `c`
- (4) Make `c` as the parent of `a`.



## Reference
- [AVL tree \- Wikipedia](https://en.wikipedia.org/wiki/AVL_tree)
- https://www.programiz.com/dsa/avl-tree
- https://www.ics.uci.edu/~goodrich/teach/cs260P/notes/AVLTrees.pdf
