# Algorithm Notebook

## Trees

### In Order Traversal

Traversal in the order: left subtree -> root -> right subtree

1. If a left child of root exists, run InOrder on left child
2. Print out the root
3. If a right child of root exists, run InOrder on right child

### Pre Order Traversal

Traversal in the order: root -> left subtree -> right subtree

1. Print out the root
2. If a left child of root exists, run PreOrder on left child
3. If a right child of root exists, run PreOrder on right child

### Post Order Traversal

Traversal in the order: left subtree -> right subtree -> root

1. If a left child of root exists, run PostOrder on left child
2. If a right child of root exists, run PostOrder on right child
3. Print out the root

### Depth First Traversal

#### Iterative

1. Use a stack
2. While the stack is not empty, pop the last element from the stack and store the value in a variable (i.e current)
3. Print out the value of current (or store it in an array)
4. If current's right child exists, add it to the stack
5. If the current's left child exists, add it to the stack
