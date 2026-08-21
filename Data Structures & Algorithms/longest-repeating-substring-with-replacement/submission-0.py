class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        max_count = 0
        left = 0
        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right],0)+1

            while (right-left+1) - max(seen.values()) > k:
                seen[s[left]] -= 1
                left += 1
            max_count = max(max_count,right-left+1)
        return max_count