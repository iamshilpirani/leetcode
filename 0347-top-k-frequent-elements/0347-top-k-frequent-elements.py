class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        items = list(d.items()) 
        items.sort(key=lambda x: x[1],reverse=True)
        ans = []
        for key, value in items:
            if k > 0:
                ans.append(key)
                k -=1
            else:
                break
        return ans