class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        nums=[(nums[i], i)for i in range(len(nums))]
        nums.sort()
        left=0
        right=len(nums)-1
        while(left<right):
            s=nums[left][0]+nums[right][0]
            if (s==target):
                result.append(nums[left][1])   
                result.append(nums[right][1])
                break
            elif s>target:
                right=right-1
            else:
                left=left+1
        return result
        
