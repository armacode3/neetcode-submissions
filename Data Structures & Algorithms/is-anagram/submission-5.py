class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if both strings are same length, if not then can't be anagram
        if len(s) != len(t):
            return False

        # Create two dicts for both strings
        seenS, seenT = {}, {}

        # Loop through length of string and add character as key
        for i in range(len(s)):
            # .get specific character and value + 1 since seen again
            seenS[s[i]] = 1 + seenS.get(s[i], 0)
            seenT[t[i]] = 1 + seenT.get(t[i], 0)

        # Compare both dictionaries, if not same then not anagram
        return seenS == seenT


