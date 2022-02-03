class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = -10**4
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum < nums[i]:
                current_sum = nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum
