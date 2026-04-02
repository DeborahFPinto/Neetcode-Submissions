class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        output = 0

        for i in range(len(nums)):
            
            continueLoop = 1
            temp = nums[i]
            pos = i
            cont = 1

            while continueLoop:
                if (temp + 1) in nums:
                    temp += 1
                    pos = nums.index(temp)
                    cont += 1
                else: 
                    continueLoop = 0
                    if cont > output:
                        output = cont

        return output
    
