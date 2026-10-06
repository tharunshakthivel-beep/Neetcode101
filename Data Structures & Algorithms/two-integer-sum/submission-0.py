class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        elem={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in elem:
                l.append(elem[diff])
                l.append(i)
            elem[nums[i]]=i
        return l