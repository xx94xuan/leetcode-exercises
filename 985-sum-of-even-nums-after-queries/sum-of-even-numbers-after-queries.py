class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for i in queries:
            val = i[0]
            index = i[1]
            A[index] += val
            even_nums = []
            for num in A:
                if num % 2 ==0:
                    even_nums.append(num)
            res.append(sum(even_nums))
        return(res)
