class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        char_set = set(s)

        for c in char_set:
            count = 0
            left = 0

            # count each matching letter with right pointer
            for right in range(len(s)):
                if s[right] == c:
                    count += 1

                # (right - left + 1) is the window and we are trying to find the characters that aren't the same as our count
                # if its greater than k that means it will not be valid answer since thats more replacements that target k
                while (right - left + 1) - count > k:
                #since it is invalid we shrink the window by reseting counter and moving the left pointer to the right to make it valid again
                    if s[left] == c:
                        count -= 1
                    left += 1
                #update current valid window
                res = max(res, right - left + 1)

        return res