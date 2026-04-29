class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numset = set(nums)

        i = 1
        while True:
            if i not in numset:
                return i
            i += 1
        

