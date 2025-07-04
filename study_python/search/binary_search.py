
def binary_search(arr, target):

    if not list and type(target) != int:
        return -1

    left = 0
    right = len(arr) -1

    while left <= right:

        mid = (left + right)//2

        if arr[mid] == target:
            return mid

        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':

    list = [1,3, 4,6, 8]
    target = 3
    index = binary_search(list, target)
    print(index)
