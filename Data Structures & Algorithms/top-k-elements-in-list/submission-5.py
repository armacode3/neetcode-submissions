class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create frequency array with empty arrays of size length of nums
        freq = [[] for i in range(len(nums) + 1)]
        count = {} # Hashmap that will store counts of every number

        for n in nums:
            # Gets current count of number and adds 1, if no count then becomes 1
            count[n] = 1 + count.get(n, 0)

        # Loop throught the items in count
        for n, c in count.items():
            # Append the number that matches with the count in frequency
            freq[c].append(n)

        print(freq)

        # Final result list
        res = []
        # Step backward and in range of length of freq - 1 -> 0
        for i in range(len(freq) - 1, 0, -1):
            # Go through every number in freq array
            for n in freq[i]:
                # Append the number to result array
                res.append(n)
                # If the result matches with number of most frequent return
                if len(res) == k:
                    return res