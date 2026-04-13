class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        # we want to encode by counting the length of each string and adding how many chars are in
        # ex: neet = 4 , 4#neet
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            i = j + 1

            j = i + length

            res.append(s[i:j])

            i = j

        return res


