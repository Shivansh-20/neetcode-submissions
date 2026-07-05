class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set  = set(nums)
        max_streak = 0

        for nums in n_set:

         if nums-1 not in n_set:
            current_n = nums
            current_streak = 1

            while current_n + 1 in n_set:
                current_n +=1
                current_streak+=1
            max_streak = max(max_streak, current_streak)
        return max_streak

''' max_l = 0
        se  = set()
        for i in nums:
            if i not in se:
                se.add(i)
                max_l += 1

                #cond for consecutive another variable
            else:
                #what if duplicate come -> pass'''
        


        