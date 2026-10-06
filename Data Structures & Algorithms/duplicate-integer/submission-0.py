class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet=set()
        for k in nums:
            if k in hashSet:
                return True
            hashSet.add(k)
        return False