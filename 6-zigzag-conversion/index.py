class Solution:
    def convert(self, s: str, numRows: int) -> str:
        originArr = list(s)
        strLength = len(originArr)
        # res = [0] * strLength 
        res = []
        # r = 0
        if numRows >= strLength or numRows == 1:
            return s
        for i in range(numRows):
            newIndex = i
            count = 0
            # res[r] = originArr[i]
            # print(f"{r} ----------> {i}")
            res.append(originArr[i])
            # r += 1
            while newIndex < strLength:
                if count % 2 == 0:
                    skipNum = 2 * (numRows - i) - 2
                else:
                    skipNum = 2 * i
                if newIndex + skipNum >= strLength:
                    break
                elif skipNum > 0:
                    newIndex += skipNum
                    # res[r] = originArr[newIndex]
                    # print(f"{r} ------{skipNum}----> {newIndex}")
                    res.append(originArr[newIndex])
                    # r += 1
                count += 1
        return ''.join(res)
        
#          From others
        # if numRows == 1:
        #     return s 
        # n = len(s)
        # cycle = 2*numRows - 2
        # strlist = []
        # for i in range(numRows):
        #     for j in range(i, n, cycle):
        #         strlist.append(s[j])
        #         if i != numRows-1 and i != 0 and j+cycle-2*i < n:
        #             strlist.append(s[j+cycle-2*i])             
        # newstr = ''.join(strlist)
        # return newstr
