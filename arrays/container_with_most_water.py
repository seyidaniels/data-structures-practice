
def maxArea(height) -> int:
    MAX = 0
    x = len(height) - 1
    y = 0
    while x != y:
        if height[x] > height[y]:
            area = height[y] * (x - y)
            y += 1
        else:
            area = height[x] * (x - y)
            x -= 1
        MAX = max(MAX, area)
    return MAX


p = maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])

print(p)
