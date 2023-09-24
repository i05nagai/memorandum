---
title: Tree
---

## Tree


## Tree traversal

preorder

```
function dfs(root) {
    root.val;
    dfs(root.left);
    dfs(root.right);
}
```

inorder

```
function dfs(root) {
    dfs(root.left);
    root.val;
    dfs(root.right);
}
```

postorder

```
function dfs(root) {
    dfs(root.left);
    dfs(root.right);
    root.val;
}
```

## Reference
