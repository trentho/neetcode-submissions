class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        count = {}

        for num in nums:
            count[num] = count.get(num,0) + 1


        for num, freq in count.items():
            if freq > (len(nums) / 3):
                res.append(num)
        
        return res