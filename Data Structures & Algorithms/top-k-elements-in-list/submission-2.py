class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        freq = [[] for i in range(len(nums))]
        for num in nums:
            res[num] = 1 + res.get(num, 0)
        for key, val in res.items():
            freq[val-1].append(key)
        result = []
        for i in range(len(freq)-1, -1, -1):
            for f in freq[i]:
                result.append(f)
                if len(result) == k:
                    return result