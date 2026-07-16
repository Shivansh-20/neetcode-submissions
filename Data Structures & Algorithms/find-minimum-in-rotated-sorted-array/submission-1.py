class Solution:
    def findMin(self, nums: List[int]) -> int:
        #one half of array is always sorted and sorted means left side smaller
        low  = 0
        high = len(nums) - 1
        ans = float('inf')
        while low<= high:
            mid = (low+high)//2
            if nums[low] <= nums[mid]:
                ans = min(nums[low],ans)
                low = mid + 1
            elif nums[mid] <= nums[high]:
                ans = min(nums[mid],ans)
                high = mid - 1
        return ans
            


        