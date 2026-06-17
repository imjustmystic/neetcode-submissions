class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            comp = target-i
            for j in range(nums.index(i)+1,len(nums)):
                if nums[j]==comp:
                    return [nums.index(i),j]