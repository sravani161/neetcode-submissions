class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        sorted_nums = sorted(set(nums))
        count = 1
        max_count = 1
        for i in range(1,len(sorted_nums)):
            if sorted_nums[i] - sorted_nums[i-1] == 1:
                count += 1
                max_count = max(max_count,count)
            else:
                count = 1
            
        return max_count