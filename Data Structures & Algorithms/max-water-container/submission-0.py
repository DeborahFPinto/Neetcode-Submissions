class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea = 0

        for i in range(len(heights)):
            
            for j in range(i + 1, len(heights)):
                
                if heights[i] < heights[j]:
                    minHeight = heights[i] 
                else:
                    minHeight = heights[j]

                area = minHeight * (j - i)

                if area > maxArea:
                    maxArea = area
        
        return maxArea