class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for index in range(len(nums)):
            if target-nums[index] not in Map:
                Map[nums[index]] = index
            else:
                return [Map[target-nums[index]],index]
            
