class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s += st
            s +="~"
        return s
    def decode(self, s: str) -> List[str]:
        ret = s.split("~")
        return ret[:len(ret)-1]
            
