class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}

        for i in s:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        
        for i in t:
            if i in seen:
                seen[i] -= 1
            else:
                return False
        
        for val in seen.values():
            if val != 0:
                return False

        print(seen)

        return True
