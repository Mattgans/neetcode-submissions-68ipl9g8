class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for word in strs:
            code += word + "`"
        print(code)
        return code

    def decode(self, s: str) -> List[str]:
        words = s.split("`")
        return list(words)[:-1]