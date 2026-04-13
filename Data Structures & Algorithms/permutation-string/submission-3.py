class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # cant contain permutation if s1 is larger than s2
        if len(s1) > len(s2):
            return False

        s1count = [0] * 26
        s2count = [0] * 26
        
        # map letters a-z to each index of the list
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1

        # count matching characters at each index
        matching = 0
        for i in range(26):
            if (s1count[i] == s2count[i]):
                matching += 1
        
        left = 0

        for right in range(len(s1), len(s2)):
            # if there are exact 26 matches 1:1 characters then must be true
            if matching == 26:
                return True

            #Add the character at s2[r] (right end of the window) to the s2Count frequency.
            index = ord(s2[right]) - ord('a')
            s2count[index] += 1

# If the frequency of the character now matches s1Count, increment matches.
# This means the added character brings the two counts into alignment.
# If the frequency of the character exceeds s1Count by 1, decrement matches.
# This means adding the character broke the alignment.
            if s1count[index] == s2count[index]:
                matching += 1
            elif s1count[index] + 1 == s2count[index]:
                matching -= 1

        #Add the character at s2[left] (left end of the window) to the s2Count frequency.

            index = ord(s2[left]) - ord('a')

            s2count[index] -= 1

            if s1count[index] == s2count[index]:
                matching += 1

            elif s1count[index] - 1 == s2count[index]:
                matching -= 1

            left += 1
        return matching == 26
        
             