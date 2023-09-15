# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return []
    def bfs(self, root):
        queue = [ root ]
        ret = []
        while len(queue) > 0:
            
sol = Solution()

L1 = TreeNode(1)
L2 = TreeNode(2)
L3 = TreeNode(3)
L4 = TreeNode(4)
L5 = TreeNode(5)

L1.left = L2
L1.right = L3
L3.left = L4
L2.right = L5

print(sol.bfs(L1))
        
            