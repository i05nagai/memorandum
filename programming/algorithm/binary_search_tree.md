---
title: Binary Search Tree
---

## Binary Search Tree

## Add

## Remove
* (1) To ensure the constraints of BST, you need to replace removed node with the maxium value of descendants of the left child or the least value in descendants of the right child
    * For simplicity, we use the maximum value of the descendants of the left child
    * (1-1)
        * the left child doesn't exist
        * -> the right node can be replaced with the removed node
    * (1-2) 
        * the left node exists
        * the right child of left child doesn't exist
        * -> the right child of left child can be replaced with the removed node
    * (1-3) 
        * the left node exists
        * the right child of left child exists
        * -> the maximum value is the last right child


## Reference
* [Binary Search Trees](https://www.cs.auckland.ac.nz/courses/compsci220s1c/lectures/2016S1C/CS220-Lecture14.pdf)
