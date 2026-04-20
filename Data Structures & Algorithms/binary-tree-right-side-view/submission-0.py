# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[]
        queue=deque([root])
        while queue:
            level_size=len(queue)
            for i in range(level_size):
                root=queue.popleft()
                if i==level_size-1:
                    res.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        return res   


                              