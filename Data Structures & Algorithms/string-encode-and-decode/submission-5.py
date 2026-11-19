class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret = ret + s + "`"
        return ret
    def decode(self, s: str) -> List[str]:
        return s.split("`")[:-1]