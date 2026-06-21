class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}

        for n in nums:
            if n in numMap:
                numMap[n] += 1
            else:
                numMap[n] = 1
        
        sorted_numMap = dict(sorted(numMap.items(), key=lambda item: item[1]))
        keys = list(sorted_numMap.keys())
        f_keys = keys[::-1]

        res = []
        for i in range(0,k):
            res.append(f_keys[i])
        return res
        