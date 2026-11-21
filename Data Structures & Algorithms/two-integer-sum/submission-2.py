class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in elements:
                return [elements[diff], i]
            elements[n] = i
