class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}
        for n in nums:
            if n in numsMap:
                numsMap[n]+=1
            else:
                numsMap[n] = 1
        numsMap = dict(sorted(numsMap.items(),key = lambda item:item[1]))
        res =  list(numsMap.keys())
        #print()
        return res[len(res)-k:len(res)]

        