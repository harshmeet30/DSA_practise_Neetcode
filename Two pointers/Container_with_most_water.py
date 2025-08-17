class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxArea = 0
        while l!=r:
            if height[l] < height[r]:
                maxArea = max(maxArea, min(height[l],height[r])*(r-l))
                l+=1
            else:
                maxArea = max(maxArea, min(height[l],height[r])*(r-l))
                r-=1
        return maxArea


# Brute Force -
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         maxarea=0
#         for i in range(len(height)):
#             for j in range(i+1,len(height)):
#                     maxarea = max(maxarea, (min(height[i],height[j]))*(j-i) )
#         return maxarea
