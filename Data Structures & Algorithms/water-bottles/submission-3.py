class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # if numBottles < numExchange:
        #     return numBottles
        # count = numBottles
        # empty = numBottles
        # while(empty >= numExchange):
        #     empty -= (numExchange - 1)
        #     count += 1
        # return count

        return numBottles + (numBottles - 1) // (numExchange - 1)
