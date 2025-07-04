
def selection_sort(arr):

    if not arr or len(arr) == 0:
        return
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                arr[j], arr[min_index]= arr[min_index], arr[j]




    return arr


if __name__ == '__main__':
    arr = [1, 3, 4, 5, 2]
    sorted_arr = selection_sort(arr)

    print(sorted_arr)
