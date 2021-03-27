class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # 1
        length = len(bits) - 1
        i = 0
        while i < length:
            if bits[i] > 0:
                i = i + 2
            else:
                i = i + 1
        # if i == length:
        #     return True
        # else:
        #     return False
        return i == length
        
        
        # From others:
        # i = 0
        # while i < len(bits) - 1:
        #     i += bits[i] + 1
        # return i == len(bits) - 1
            
