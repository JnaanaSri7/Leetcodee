class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=0
        curr_max=nums[0]
        for i in range(1,len(nums)):
            res=max(res,(curr_max-1)*(nums[i]-1))
            curr_max=max(curr_max,nums[i])
        return res
