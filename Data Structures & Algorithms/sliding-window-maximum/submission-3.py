class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        listMaiores = []

        for i in range(len(nums) - k + 1):
            
            maior = -10000
            
            for j in range(k):
                if nums[i + j] > maior:
                    maior = nums[i + j]
            
            listMaiores.append(maior)
        
        return listMaiores