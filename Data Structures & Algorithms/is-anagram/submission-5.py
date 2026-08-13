class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : 
            return False 
        else : 
            dic1, dic2 = {},{}
            for ch in s : 
                dic1[ch] = dic1.get(ch,0)+1
            for ch in t : 
                dic2[ch] = dic2.get(ch,0)+1
            return dic1 == dic2 