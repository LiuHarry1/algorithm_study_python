
def contain(list, b):

    for i  in list:
        if i == b:
            return True
    return False



def binary_searh(arr, target):

    if len(arr) == 0 :
        return -1

    if len(arr) == 1:
        if arr[0] == target:
            return 0
        return -1


    start = 0;
    end = len(arr) -1

    while (start <= end):
        middle = (end + start)//2
        if arr[middle] == target:
            return middle

        if arr[middle] <target:
            start = middle +1
        else:
            end = middle -1

    return -1


if __name__ == '__main__':

    list = [1, 2, 3, 4]
    b = 2
    # print(contain(list, b))

    print(binary_searh(list, b))