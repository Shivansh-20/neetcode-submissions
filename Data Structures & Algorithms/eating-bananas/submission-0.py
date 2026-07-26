from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low+high)//2
            k = self.spd(piles,mid)
            if k <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low
    def spd(self,piles,mid):
            tmp = 0
            for banana in piles:
                tp = ceil(banana/mid)
                tmp += tp
            return tmp
            
        