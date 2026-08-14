class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        leftCount = 1
        rightCount = 1
        
        for i in range(len(nums)):
            leftCount *= nums[i]
            rightCount *= nums[len(nums)-1 -i]
            
            left[i] = leftCount
            right[len(nums) -1 -i] = rightCount
        
        res = [0] * len(nums)

        for i in range(len(nums)):
            ln = 1
            rn = 1
            if i > 0:
                ln = left[i-1]
            if i < len(nums) -1:
                rn = right[i+1]
            res[i] = ln * rn
        
        return res


