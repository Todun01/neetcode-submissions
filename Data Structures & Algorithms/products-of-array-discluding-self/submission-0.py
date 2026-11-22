class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        for i in range(len(nums)-1):
            res.append(res[-1]*nums[i])
        postfix = 1
        for i in range(len(res)-1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]
        return res