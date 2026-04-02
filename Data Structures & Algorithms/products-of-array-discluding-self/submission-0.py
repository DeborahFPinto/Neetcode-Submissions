class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        multiply = []
        tam = len(nums)

        for i in range(tam):
            multiply.append(1)

        for i in range(tam):
            for j in range(tam):
                if i == j:
                    pass
                else:
                    multiply[i] = multiply[i]*nums[j]
        
        return multiply