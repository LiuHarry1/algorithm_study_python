
def quick_sort(arr):

    if len(arr) <=1:
        return arr

    povit = arr[0]

    left = [x for x in arr if x < povit]
    mid = [x for x in arr if x == povit]
    right = [x for x in arr if x > povit]

    return quick_sort(left) + mid + quick_sort(right)


if __name__ == '__main__':
    arr = [1, 7, 6, 3, 3,4, 5]

    result = quick_sort(arr)
    print(result)
