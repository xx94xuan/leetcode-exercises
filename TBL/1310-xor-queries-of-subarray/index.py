class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Time Limit Exceeded:
        # result = []
        # for query in queries:
        #     startIndex = query[0]
        #     endIndex = query[1] + 1
        #     resArr = arr[startIndex:endIndex]
        #     xor = resArr[0]
        #     for i in range(1, len(resArr)):
        #          xor = xor ^ resArr[i]
        #     result.append(xor)
        # # print(result)
        # return result
        

        # !!!!! 0 ^ n = n; n ^ n = 0; 0 ^ 0 = 0 !!!!!

        prefix = [0] + arr.copy()
        for i in range(len(arr)):
            prefix[i+1] ^= prefix[i]
        res = []
        for left, right in queries:
            res.append(prefix[left] ^ prefix[right+1])
        return res
        
        # From others
        # prefix = [0] + arr.copy()
        # for i in range(len(arr)):
        #     prefix[i+1]^=prefix[i]
        # ans = []
        # for left,right in queries:
        #     ans.append(prefix[right+1]^prefix[left])
        # return ans
        

        