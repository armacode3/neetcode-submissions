class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}
        for i in range(len(nums)):
            storage[nums[i]] = i

        print(storage)

        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in storage and i != storage[sub]:
                return [i, storage[sub]]
        return [0,0]
            