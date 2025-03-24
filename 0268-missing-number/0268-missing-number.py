class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = sorted(nums)
        Sum = 0
        for i in num:
            Sum += i

        a = 0
        for i in range(0,len(num)+1):
            a += i
        return a - Sum    

        