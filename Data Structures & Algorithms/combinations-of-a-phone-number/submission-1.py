class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []

        # map digit to each corresponding chars

        digit_to_char = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }


        def backtrack(i, current_string):
            # base case since current string cannot be longer than the size of digits
            if len(current_string) == len(digits):
                res.append(current_string)
                return

            # back track for each letter in our map
            for c in digit_to_char[digits[i]]:
                backtrack(i + 1, current_string + c)




        if digits:
            backtrack(0, "")

        return res