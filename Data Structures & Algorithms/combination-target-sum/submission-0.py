class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def dfs(i, cur, total):
            # we found our answer make a copy and append to res
            if total == target:
                res.append(cur.copy())
                return

            # we are out of bounds so return immediately
            if i >= len(nums) or total > target:
                return

            # append current number we are going through decision tree
            cur.append(nums[i])
            # go down our first decision tree including duplicates
            dfs(i, cur, total + nums[i])
            # clean up data by popping current
            cur.pop()

            dfs(i + 1, cur, total)

        dfs(0,[],0)
        return res