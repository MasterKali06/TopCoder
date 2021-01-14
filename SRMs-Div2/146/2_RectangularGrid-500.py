"""
Problem Statement
Given the width and height of a rectangular grid, return the total number of rectangles (NOT counting squares)
that can be found on this grid. For example, width = 3, height = 3 (see diagram below):
 __ __ __
|__|__|__|
|__|__|__|
|__|__|__|

In this grid, there are 4 2x3 rectangles, 6 1x3 rectangles and 12 1x2 rectangles.
there is a total of 4 + 6 + 12 = 22 rectangles. Note we don't count 1x1, 2x2 and 3x3 rectangles because they are squares

 
Class: RectangularGrid
Method: countRectangles
Parameters: integer, integer
Returns: long integer
Method signature: def countRectangles(self, width, height):

Notes
-	rectangles with equals sides (squares) should not be counted.

Constraints
-	width and height will be between 1 and 1000 inclusive.

Examples
0)
3
3
Returns: 22
See above

1)
5
2
Returns: 31
 __ __ __ __ __
|__|__|__|__|__|
|__|__|__|__|__|

In this grid, there is one 2x5 rectangle, 2 2x4 rectangles, 2 1x5 rectangles, 3 2x3 rectangles, 4 1x4 rectangles,
6 1x3 rectangles and 13 1x2 rectangles. Thus there is a total of 1 + 2 + 2 + 3 + 4 + 6 + 13 = 31 rectangles.

2)
10
10
Returns: 2640

3)
1
1
Returns: 0

4)
592
964
Returns: 81508708664
"""


class RectangularGrid:
    def countRectangles(self, width, height):
        if width > height:
            width, height = height, width

        squar_sum = 0
        x = 1
        while x <= width:
            squar_sum += ((height - (x - 1)) * (width - (x - 1)))
            x += 1

        rectangles = ((height * (height + 1)) * (width * (width + 1))) / 4
        return int(rectangles - squar_sum)
