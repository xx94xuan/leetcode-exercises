class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newNums = nums[0:n]
        for i in range(n):
            newNums.insert(i*2 + 1, nums[n + i])
        return newNums