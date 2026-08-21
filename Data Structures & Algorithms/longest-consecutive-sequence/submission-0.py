class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set()
        count = 0
        highest = 0
        cur = 0
        for num in nums:
            mySet.add(num)
        for num in mySet:
            if num - 1 not in mySet:
                cur = num
                count = 0
                while(cur in mySet):
                    count += 1
                    highest = max(highest, count)
                    cur += 1
        return highest