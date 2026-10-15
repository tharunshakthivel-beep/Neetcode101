class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        prev_a=0
        while(l<r):
            w=r-l
            h=min(heights[l],heights[r])
            curr_a=w*h
            prev_a=max(prev_a,curr_a)
            if(heights[l]<heights[r]):
                l+=1
            else:
                r-=1
        return prev_a