class Solution:

    def encode(self, strs: List[str]) -> str:
        newchar = ''
        for word in strs:
            delim = len(word)
            newchar = newchar + str(delim) + "#" + word 
        return newchar 


            

    def decode(self, s: str) -> List[str]:
        i=0
        lst = []
        while i < len(s): 
            j = s.find('#',i)
            length = int(s[i:j])
            lst.append(s[j+1:length+1+j])
            i = length+1+j
        return lst
            

