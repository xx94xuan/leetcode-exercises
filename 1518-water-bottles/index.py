class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        fullBottles = numBottles
        while numBottles >= numExchange:
            # full = int(numBottles / numExchange)
            full = numBottles // numExchange
            numBottles = full + numBottles % numExchange
            fullBottles += full
        # print(fullBottles)
        return fullBottles




# int1 // int2
# int(int1 / int2)
