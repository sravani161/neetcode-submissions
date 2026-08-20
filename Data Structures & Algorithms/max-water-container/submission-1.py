class Solution:
    def maxArea(self, heights: List[int]) -> int:
        first = 0
        last = len(heights)-1
        max_area = 0
        while first < last:
            area = min(heights[first],heights[last])*(last-first)
            max_area = max(max_area,area)
            if heights[first] < heights[last]:
                first += 1
            else:
                last -= 1
            

        return max_area
