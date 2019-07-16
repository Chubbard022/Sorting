# TO-DO: complete the help function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    arrayA_index = 0
    arrayB_index = 0 
    merge_index = 0

    while arrayA_index < len(arrA) and arrayB_index < len(arrB):
        if arrA[arrayA_index] < arrB[arrayB_index]:
            merged_arr[merge_index] = arrA[arrayA_index]
            arrayA_index += 1
        else:
            merged_arr[merge_index] = arrB[arrayB_index]
            arrayB_index += 1
            merge_index += 1
    while arrayA_index < len(arrA):
        merged_arr[merge_index] = arrA[arrayA_index]
        arrayA_index += 1
        merge_index += 1
    while arrayB_index < len(arrB):
        merged_arr[merge_index] = arrB[arrayB_index]
        arrayB_index += 1
        merge_index += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle_index = len(arr)//2
    left_array = merge_sort(arr[:middle_index])
    right_array = merge_sort(arr[middle_index:])
    sort_arr = []
    left_index = 0
    right_index = 0

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            sort_arr.append(left_array[left_index])
            left_index += 1
        else:
            sort_arr.append(right_array[right_index])
            right_index += 1
    sort_arr += left_array[left_index:]
    sort_arr += right_array[right_index:]
    return sort_arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
