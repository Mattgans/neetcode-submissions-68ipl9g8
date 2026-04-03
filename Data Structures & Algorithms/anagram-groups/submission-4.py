class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            counts = [0] * 26
            for letter in word:
                index = ord(letter) - ord("a")
                counts[index] += 1
            key = tuple(counts)
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        
        return list(groups.values())

                     
            
           