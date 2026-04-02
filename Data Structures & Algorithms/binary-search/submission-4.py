class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        half = int(len(nums)/2)
        upper_limit = len(nums)
        lower_limit = 0
        
        temp = len(nums)
        tam = 0
        while  temp > 0:
            tam += 1
            temp = temp >> 1

        for i in range(tam+1):
            
            half = int((upper_limit + lower_limit)/2)

            if nums[half] == target:
                return half
            elif nums[half] > target:
                upper_limit = half
            elif nums[half] < target:
                lower_limit = half
        
        return -1