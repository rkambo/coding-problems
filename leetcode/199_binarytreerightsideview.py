def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    queue = [root]
    ret = []
    while queue:
        rightSide = None
        qLen = len(queue)
        for i in range(qLen):
            current = queue.pop(0)
            if current:
                rightSide = current
                queue.append(current.left)
                queue.append(current.right)
        if rightSide:
            ret.append(rightSide.val)
    return ret
        
            