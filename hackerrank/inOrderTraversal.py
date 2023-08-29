def inOrder(root):
    if root.left != None:
        inOrder(root.left)
    print(root.info, end = " ")
    if root.right != None:
        inOrder(root.right)