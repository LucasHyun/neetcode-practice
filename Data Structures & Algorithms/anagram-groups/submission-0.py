class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #일단 set으로 해결해야하지 않을까?
        groups = {}

        for word in strs:
            key = "".join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]


        return list(groups.values())
                    
