class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Map1 = Counter(s)
        Map2 = Counter(t)
        return Map1 == Map2