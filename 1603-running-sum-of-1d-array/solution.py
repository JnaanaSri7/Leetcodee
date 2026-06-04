class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[]
        s=0
        for num in nums:
            s=s+num
            result.append(s)
        return result
