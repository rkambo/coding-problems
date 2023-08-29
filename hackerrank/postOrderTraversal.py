def postOrder(root):
    if root.left != None:
        postOrder(root.left)
    if root.right != None:
        postOrder(root.right)
    print(root.info, end = " ")