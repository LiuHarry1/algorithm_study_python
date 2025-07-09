
def maxArea(heights):

    left =0
    right = len(heights)-1

    max_area = 0
    while left < right:
        h = min(heights[left], heights[right])
        w = right -left

        area = h * w

        max_area = max(max_area, area)

        if heights[left] > heights[right]:
            right -=1
        else:
            left +=1

    return max_area

if __name__ == '__main__':
    heights = [1,8,6,2,5,4,8,3,7]
    result = maxArea(heights)
    print(result)
