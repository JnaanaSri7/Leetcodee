class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count=Counter(nums)
        ans=0
        for (key,val)in count.items():
            if val==1:
                ans+=key
        return ans

