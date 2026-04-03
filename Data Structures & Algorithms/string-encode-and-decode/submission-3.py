class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += s + "~"
        return ret
    def decode(self, s: str) -> List[str]:
        ret = []
        add = ""
        for val in s:
            if val != "~":
                add += val
            else:
                ret.append(add)
                add = ""
        return ret
