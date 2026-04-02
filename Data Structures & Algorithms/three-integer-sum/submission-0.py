class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        listTriplets = []
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                
                numsSlice = nums[j + 1 : len(nums)]
                k = (nums[i] + nums[j])*-1

                if k in numsSlice:
                    triplet = [nums[i], nums[j], k]
                    triplet.sort()
                    if triplet not in listTriplets:
                        listTriplets.append(triplet)
                        pass
            
           

        return listTriplets