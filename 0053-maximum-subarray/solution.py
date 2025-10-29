class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=0
        maxsum=float('-inf')
        for num in nums:
            s+=num
            if s>maxsum:
                maxsum=s
            if s<0:
                s=0
        return maxsum
        
