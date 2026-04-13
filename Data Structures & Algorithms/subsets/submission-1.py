class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subsets = []


        def backtrack(i):
            # base case where we get to the end of nums
            if i >= len(nums):
                res.append(subsets.copy()) # store the subset . Ex = [1,2,3]
                return
            
            subsets.append(nums[i])

            backtrack(i + 1)

            subsets.pop()

            backtrack(i + 1)






        backtrack(0)
        return res