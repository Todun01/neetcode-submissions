class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        copy = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in copy:
                length = 0
                while num + length in copy:
                    length += 1
                longest = max(length, longest)
        return longest
            
            


            
