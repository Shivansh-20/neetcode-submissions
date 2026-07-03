class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i ,x in enumerate(nums):
         l = target - x
         if l in seen:
             return [seen[l], i]
         seen[x] = i
        '''for x,y in enumerate(nums):
            seen[y] = x
        for i in range(len(nums)): #to make i as index , range and len if not then i is values of num
            c = target - nums[i]
            if c in seen and seen[c] != i:
                return (sorted([seen[c], i]))'''
            


            