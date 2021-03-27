from itertools import accumulate as acc

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        #1
        r_num = 0
        l_num = 0
        res = 0
        for c in s:
            if c == 'R':
                r_num += 1
            elif c == 'L':
                l_num += 1
            if r_num != 0 and r_num == l_num:
                res += 1
        return res
        
        #2
        d = {'R': 0, 'L': 0}
        res = 0
        for c in s:
            d[c] += 1
            if d['R'] == d['L']:
                res += 1
        return res
        
        #From others

        #one line
        return list(acc(1 if c == 'L' else -1 for c in s)).count(0)

        # (True = 1)
        res = cnt = 0         
        for c in s:
            cnt += c == 'L'
            cnt -= c == 'R'
            res += cnt == 0
        return res
        
        
        
        