class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}


        for num in nums:
            count[num] = count.get(num, 0) + 1

        
        for number, count in count.items():
            if count > len(nums) / 2:
                return number
        