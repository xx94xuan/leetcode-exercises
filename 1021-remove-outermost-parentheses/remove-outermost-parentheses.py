class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        tmp = 0
        result = ''
        pre_ind = 0
        for index, p in enumerate(S):
            if p == '(':
                tmp += 1
            else:
                tmp -= 1
            if tmp == 0:
                result += S[pre_ind+1:index]
                # pri_lst.append(S[pre_ind+1:index])
                pre_ind = index + 1 
        # print(result)
        return result
        
        