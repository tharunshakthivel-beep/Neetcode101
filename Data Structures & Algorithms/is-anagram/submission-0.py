class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        for ch1 in s:
            d1[ch1]=d1.get(ch1,0)+1
        for ch2 in t:
            d2[ch2]=d2.get(ch2,0)+1
        if(d1==d2):
            return True
        else:
            return False