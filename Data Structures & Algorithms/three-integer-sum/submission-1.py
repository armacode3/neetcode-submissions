class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Do not use same values twice
            if i > 0 and a == nums[i-1]:
                continue
            
            # Left and Right pointer
            l, r = i + 1, len(nums) - 1
            while l < r:
                # Calculate the sum and match condition
                threeSum = a + nums[l] + nums[r]
                # Because array is sorted we can either move down or up
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # This means it's a correct solution
                    res.append([a, nums[l], nums[r]])
                    # Update left pointer and make sure next left number is not the same
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res