class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l = 0
        while l < len(nums):
            if l > 0 and nums[l] == nums[l-1]:
                    return True
            l += 1
        return False