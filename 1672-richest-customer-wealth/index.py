class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0
        for a in accounts:
            if max_sum < sum(a):
                max_sum = sum(a)
        return max_sum
