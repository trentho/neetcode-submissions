class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #intialize two pointers
        left, right = 0, len(numbers) - 1
        
        while left < right:
            #get current sum
            current_sum = numbers[left] + numbers[right]

            #check to see if current sum equals target
            if current_sum == target:
                return [left + 1,right + 1]
            if current_sum < target:
                left += 1
            else:
                right -= 1
        return [-1,-1]