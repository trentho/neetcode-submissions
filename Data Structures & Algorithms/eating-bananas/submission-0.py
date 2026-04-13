class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)
        #intialize default to the max pile since that is upperbound of how long it will take
        res = right

        while left <= right:
            mid = (left + right) // 2

            time_taken = 0

            for p in piles:
                time_taken += math.ceil(float(p) / mid)

            if time_taken <= h:
                res = mid
                right = mid - 1

            else:
                left = mid + 1

        return res
