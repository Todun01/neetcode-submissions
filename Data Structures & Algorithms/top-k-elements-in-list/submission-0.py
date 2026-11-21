class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            elements[num] = 1 + elements.get(num, 0)
        for n, count in elements.items():
            freq[count].append(n)
        output = []
        for j in range(len(freq) - 1, 0, -1):
            for num in freq[j]:
                output.append(num)
                if len(output) == k:
                    return output

        