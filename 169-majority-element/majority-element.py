class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
            if counts[num] > len(nums) // 2:
                return num
