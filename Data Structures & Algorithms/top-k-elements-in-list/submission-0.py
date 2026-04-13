class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        freq = [ [] for i in range (len(nums) + 1)]

        # get frequency of each number if it doesnt exist init to 0 and increment by 1
        for n in nums:
            count[n] = 1 + count.get(n , 0)

        
        for num , count in count.items():
            # this value num occurs freq[count] times
            freq[count].append(num)


        res = []

        # now find top k elements

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                    