class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        odd_list = []
        for index, value in enumerate(sorted(nums)):
            if index % 2 == 0:
                odd_list.append(value)
        return(sum(odd_list))
