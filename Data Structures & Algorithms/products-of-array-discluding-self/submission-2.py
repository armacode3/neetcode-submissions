class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in range(len(nums))]

        pref = 1
        for i in range(len(nums)):
            res[i] = pref
            pref *= nums[i]

        posf = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= posf
            posf *= nums[i]

        return res