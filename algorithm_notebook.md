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

Note: DFT can be done iteratively or recursively, as it uses a stack (which is what is used under the hood in recursion)

#### Iterative

1. Use a stack
2. While the stack is not empty, pop the last element from the stack and store the value in a variable (i.e current)
3. Print out the value of current (or store it in an array)
4. If current's right child exists, add it to the stack
5. If the current's left child exists, add it to the stack

#### Recursive

1. If the root is null, return an empty array
2. Call DepthFirstTraversal on the left child, save the output (Saving is optional as you can call the method itself in the return)
3. Call DepthFirstTraversal on the right child, save the output
4. Return the concat of the root value, the DFT of the left tree, and the DFT of the right tree

### Breadth First Traversal

Note: Unlike DFT, BFT _can't_ use recursion, as it uses a queue, **not** a stack

#### Iterative

1. Check if root is null, return empty array
2. Otherwise, use a queue
3. While the queue is not empty, dequeue the first element from the stack
4. Print out the value of current (or store it in an array)
5. If the current's left child exists, add it to the queue
6. If the current's right child exists, add it to the queue
