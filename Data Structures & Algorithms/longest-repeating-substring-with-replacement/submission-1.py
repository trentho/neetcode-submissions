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

                while (right - left + 1) - count > k:
                    if s[left] == c:
                        count -= 1
                    left += 1
                res = max(res, right - left + 1)

        return res