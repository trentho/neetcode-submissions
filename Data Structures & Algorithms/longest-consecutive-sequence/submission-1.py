class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert array to a hash set
        numSet = set(nums)

        longest = 0

        for n in nums:
            #check if the current number (n) is the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                # count current number  and length of the sequence
                while (n + length) in numSet:
                    length += 1
                # update the longest to the max of current length or longest
                longest = max(length, longest)
        
        return longest