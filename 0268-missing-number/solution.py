class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        s=sum(nums)
        m=(n*(n+1)/2-s)
        return int(m)
        
