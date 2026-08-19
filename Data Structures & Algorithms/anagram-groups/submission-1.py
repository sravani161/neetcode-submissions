class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        
        for i in strs:
            if tuple(sorted(i)) in dict1:
                dict1[tuple(sorted(i))].append(i)
            else:
                dict1[tuple(sorted(i))] = [i]
        
        return list(dict1.values())