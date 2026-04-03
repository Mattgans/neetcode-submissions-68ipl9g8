class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for let in word:
                count[ord(let) - ord('a')] += 1
            key = tuple(count)
            final[key].append(word)
        return final.values()
            
