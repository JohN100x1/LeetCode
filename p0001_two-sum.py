class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        compliments = {}
        indices = []
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in compliments:
                indices = [compliments[compliment], i]
            compliments[num] = i
        return indices
