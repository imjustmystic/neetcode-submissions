class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we are checking from either sides because the array is sorted
        #initialize the two pointers
        #using two pointers because problem asks for O(1) space complexity
        #so no new storages
        l,r = 0, len(nums)-1
        #initialze the loop since only one pair exist, we can check each elemnt just once
        while (l<r):
            #return indices+1 if elements at both indicies add up to target
            added_value = nums[l] + nums[r]
            if(added_value == target):
                return [l+1,r+1]
            elif added_value > target:
                #since array is sorted if addition is > target we need too decrease the value
                #so we bring the right pointer inward
                r-=1
            else:
                #if value is less that target we increase the smaller value
                #since the array is sorted that means we increment i
                l+=1 
        