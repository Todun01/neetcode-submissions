class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache = []
        for num in nums:
            if num not in cache:
                cache.append(num)
            else:
                return True
        return False