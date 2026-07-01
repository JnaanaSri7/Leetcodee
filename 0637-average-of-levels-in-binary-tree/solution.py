# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res=[]
        if not root:   #if root is empty
            return res
        q=collections.deque()
        q.append(root)
        while q:
            same_level=[]
            for i in range(len(q)):
                node=q.popleft()
                same_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            avg=sum(same_level)/len(same_level)
            res.append(avg)
        return res
        

