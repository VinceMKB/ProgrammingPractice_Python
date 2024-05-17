import sys

class Solution(object):
    def ComputeArea(self, RectA_x1, RectA_y1, RectA_x2, RectA_y2, RectB_x1, RectB_y1, RectB_x2, RectB_y2):
        # Calculate the area of each rectangle
        area_A = abs(RectA_x2 - RectA_x1) * abs(RectA_y2 - RectA_y1)
        print(f"The area of rectangle A is : {area_A}")
        
        # Corrected calculation for the area of rectangle B
        area_B = abs(RectB_x2 - RectB_x1) * abs(RectB_y2 - RectB_y1)
        print(f"The area of rectangle B is : {area_B}")

        # Correctly find the coordinates of the intersection rectangle
        inter_x1 = max(RectA_x1, RectB_x1)
        inter_y1 = max(RectA_y1, RectB_y1)
        inter_x2 = min(RectA_x2, RectB_x2)
        inter_y2 = min(RectA_y2, RectB_y2)

        # Check if there is an intersection
        if inter_x1 < inter_x2 and inter_y1 < inter_y2:
            inter_area = abs(inter_x2 - inter_x1) * abs(inter_y2 - inter_y1)
        else:
            inter_area = 0
        
        total_area = area_A + area_B - inter_area

        return total_area
    
solution = Solution()
result = solution.ComputeArea(-3, 0, 3, 4, 0, -1, 9, 2)
print(f"The area is {result}")