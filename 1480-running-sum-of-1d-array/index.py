class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        i = 0
        for index,value in enumerate(nums):
            i += value
            res[index] =i
        return res
