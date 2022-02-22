class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        e = 0
        p = None
        for i in range(len(nums)):
            if p is None or nums[i] != p:
                nums[e] = nums[i]
                p = nums[i]
                e += 1
            else:
                continue
        return e
