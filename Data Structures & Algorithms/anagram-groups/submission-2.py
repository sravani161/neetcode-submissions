class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Map = {}
        for string in strs:
            key = tuple(sorted(string))
            if key in Map:
                Map[key].append(string)
            else:
                Map[key] = [string]
        for value in Map.values():
            return list(Map.values())