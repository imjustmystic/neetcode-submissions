class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #initiate two pointers i, j(i+1) cause they cant be same number
        i,j = 0,len(numbers)-1
        #iterate through the sorted array
        while(i<j):
            #return[i+1,j+1] cause its a 1-indexed array
            if (numbers[i]+numbers[j] == target):
                return [i+1,j+1]
            elif (numbers[i]+numbers[j] < target):
                i+=1
            else:
                j-=1
        