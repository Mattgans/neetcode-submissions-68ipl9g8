class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force
        # groups = []
        # for s in strs:
        #     s_sorted = sorted(s)
        #     added = False
        #     for group in groups:
        #         if sorted(group[0]) == s_sorted:
        #             group.append(s)
        #             added = True
        #     if added == False:
        #         groups.append([s])
        # return groups
        groups = {}
        for s in strs:
            counts = [0] * 26
            for l in s:
                counts[ord(l)-ord('a')] += 1
            key = tuple(counts)
            if key not in (groups):
                groups[key] = []
            groups[key].append(s)
        
        # print(groups)
        return list(groups.values())
