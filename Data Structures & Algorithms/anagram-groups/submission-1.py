class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #일단 set으로 해결해야하지 않을까?
        groups = {}
        #key랑 join을 사용해서 이제 집어넣는 방식.
        for word in strs:
            key = "".join(sorted(word)) #string 같은 경우는 이제 sort를 조지면 이제 제대로 안 들어감.
            #그러니까 이제 join을 이용해서 alphabet을 결합함.
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]


        return list(groups.values())
                    
