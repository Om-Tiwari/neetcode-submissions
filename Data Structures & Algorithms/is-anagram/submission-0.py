from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hashh = defaultdict(int)
        for i in range(len(s)):
            hashh[s[i]]+=1
            hashh[t[i]]-=1
        for v in hashh.values():
            if v > 0:
                return False
        return True
