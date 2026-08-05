class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        arr = [[] for i in range(len(nums) +1)]
        for num in nums:
            myDict[num] = 1 + myDict.get(num,0)

        for key, value in myDict.items():
            arr[value].append(key)

        res = []

        for i in range(len(arr) -1, -1, -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res