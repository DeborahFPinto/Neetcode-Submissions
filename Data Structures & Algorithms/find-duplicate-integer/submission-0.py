class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        tam = len(nums)
        arrSearch = []

        for i in range(tam + 1):
            arrSearch.append(0)

        for elem in nums:

            if arrSearch[elem] == 1:
                return elem
            else:
                arrSearch[elem] = 1