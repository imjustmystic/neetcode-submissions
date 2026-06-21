class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            j = len(nums)-1
            while(i<j):
                if(nums[i]+nums[j] == target):
                    return [i,j]
                else:
                    j-=1 