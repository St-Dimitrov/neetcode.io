from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        freq_map = Counter(nums)
        # Step 2: Create buckets where index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        # Step 3: Gather top k frequent elements from buckets
        result = []
        for freq in range(len(buckets) -1, -1, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
'''
solution = Solution()
nums, k = [1,2,2,3,3,3,4,4,4,5,1], 2
result = solution.topKFrequent(nums, k)
print(result)
'''