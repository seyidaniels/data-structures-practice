# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Sea(object):
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:

class Point(object):
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y


 # 1 1
 # 1 1
class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        X, Y = topRight.x - bottomLeft.x, topRight.y - bottomLeft.y

#         I do not understand why this is there 
        if X == Y == 0:
            print(topRight.x, topRight.y)
            print(bottomLeft.x, bottomLeft.y)
            print("---------------------------")
            return sea.hasShips(topRight, bottomLeft)
        if not sea.hasShips(topRight, bottomLeft):
            return 0

        if X > Y:
            half = bottomLeft.x + X // 2
            midTopRight = Point(half, topRight.y)
            midBottomLeft = Point(half + 1, bottomLeft.y)
            return self.countShips(sea, midTopRight, bottomLeft) + self.countShips(sea, topRight, midBottomLeft)

        else:
            half = bottomLeft.y + Y // 2
            print(topRight.x, topRight.y)
            print(bottomLeft.x, bottomLeft.y)
            print(half)
            print("---------------------------")
            midTopRight = Point(topRight.x, half)
            midBottomLeft = Point(bottomLeft.x, half + 1)
            return self.countShips(sea, midTopRight, bottomLeft) + self.countShips(sea, topRight, midBottomLeft)
        
        
        
#         if not sea.hasShips(topRight, bottomLeft):
#             return 0
#         if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
#             return 1
        
#         midX = ( topRight.x + bottomLeft.x ) // 2
#         midY = (topRight.y + bottomLeft.y) // 2
        
#         print(midX, midY)
        
#         return self.countShips(sea, bottomLeft, Point(midX, midY)) + self.countShips(sea, Point(bottomLeft.x, midY), Point(midX, bottomLeft.y)) + self.countShips(sea, Point(midX, midY), Point(topRight.x, midY)) + self.countShips(Point(midX, midY), topRight)
        
        