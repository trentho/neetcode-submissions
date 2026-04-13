class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0 , len(numbers) - 1


        while left < right:
            current_val = numbers[left] + numbers[right]

            if current_val == target:
                #one indexed
                return [left + 1, right + 1]
            if current_val > target:
                right -= 1
            else:
                left += 1

        return [-1,-1]