class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            product = 1

            for j in range(len(nums)):
                #if we are at the current index skip over it
                if i == j:
                    continue
                
                product *= nums[j]

            output.append(product)

        return output