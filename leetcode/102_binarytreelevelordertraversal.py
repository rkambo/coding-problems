def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    queue = [ root ]
    ret = []
    while len(queue) > 0:
        level = []
        for i in range(len(queue)):
            current = queue.pop(0)
            level.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        if len(level) > 0:
            ret.append(level)
    return ret