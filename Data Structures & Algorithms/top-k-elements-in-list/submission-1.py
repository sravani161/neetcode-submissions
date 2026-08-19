class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Map = Counter(nums)
        heap = []
        for num,freq in Map.items():
            heapq.heappush(heap,(-freq,num))
        result = []
        for i in range(k):
            freq,num = heapq.heappop(heap)
            result.append(num)
        return result



