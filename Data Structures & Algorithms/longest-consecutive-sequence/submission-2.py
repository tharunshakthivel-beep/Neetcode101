class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0
        for n in nums:
            if (n-1) not in numSet:
                length=0
                pos=0
                while n+pos in numSet:
                    length+=1
                    pos+=1
                longest=max(length,longest)
        return longest