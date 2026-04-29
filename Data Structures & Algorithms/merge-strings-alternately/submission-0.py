class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        i, j = 0,0
        res = []

        while i < n or j < m:
            if i < n:
                res.append(word1[i])
            if j < m:
                res.append(word2[j])

            j += 1
            i += 1
        return "".join(res)