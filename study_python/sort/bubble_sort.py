
def bubble_sort(arr):

    if not arr or len(arr) == 0:
        return
    arr_length = len(arr)
    for i in range(arr_length):
        for j in range(arr_length-i -1):
            if arr[j] > arr[j +1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


if __name__ == '__main__':
    arr = [1, 3, 4, 5, 2]
    sorted_arr = bubble_sort(arr)

    print(sorted_arr)
