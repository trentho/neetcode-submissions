class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq_1 = [0] * 26
        freq_2 = [0] * 26

        if len(s) != len(t):
            return False

        for c in s:
            freq_1[ord(c) - ord('a')] += 1
        

        for c in t:
            freq_2[ord(c) - ord('a')] += 1

        return freq_1 == freq_2
