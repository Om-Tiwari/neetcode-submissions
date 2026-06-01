from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashh =  defaultdict(int)
        for i in nums:
            hashh[i]+=1
            if hashh[i] > 1:
                return True
        return False
