class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        largest_tally = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                cur_num = num + 1
                tally = 1
                while cur_num in nums_set:
                    tally += 1
                    cur_num += 1
                    
                if tally > largest_tally:
                    largest_tally = tally
        
        return largest_tally
                