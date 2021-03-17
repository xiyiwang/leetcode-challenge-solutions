"""
LeetCode Challenge: Generate Random Point in a Circle
(2021-03-17)

Given the radius and x-y positions of the center of a 
circle, write a function randPoint which generates a 
uniform random point in the circle.

Note:
1. input and output values are in floating-point.
2. radius and x-y position of the center of the circle 
   is passed into the class constructor.
3. a point on the circumference of the circle is considered 
   to be in the circle.
4. randPoint returns a size 2 array containing x-position 
   and y-position of the random point, in that order.

Explanation of Input Syntax:
The input is two lists: the subroutines called and their 
arguments. Solution's constructor has three arguments, the 
radius, x-position of the center, and y-position of the center 
of the circle. randPoint has no arguments. Arguments are always 
wrapped with a list, even if there aren't any.
"""

# runtime: 140 ms (faster than 74.16%)

from random import uniform

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        x = uniform(-self.radius, self.radius)
        y = uniform(-self.radius, self.radius)
        
        while (x**2 + y**2)**(.5) > self.radius:
            x = uniform(-self.radius, self.radius)
            y = uniform(-self.radius, self.radius)
            
        return [x+self.x_center, y+self.y_center]