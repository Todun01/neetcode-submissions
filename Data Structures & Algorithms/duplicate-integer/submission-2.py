class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache = set()
        for num in nums:
            if num not in cache:
                cache.add(num)
            else:
                return True
        return False