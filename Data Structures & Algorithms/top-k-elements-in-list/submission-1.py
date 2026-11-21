class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        freq = [[] for i in range(len(nums))]
        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1
        for key in res:
            freq[res[key]-1].append(key)
        result = []
        for i in range(len(freq)-1, -1, -1):
            for j in range(len(freq[i])):
                if len(result) == k:
                    return result
                result.append(freq[i][j])
        return result