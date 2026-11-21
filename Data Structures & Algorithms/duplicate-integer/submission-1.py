class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for r in range(i+1, len(nums)):
                if nums[i] == nums[r]:
                    return True
        # for num in nums:
        #     if num not in cache:
        #         cache.append(num)
        #     else:
        #         return True
        return False