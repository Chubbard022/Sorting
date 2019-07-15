# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for next_index in range(1,len(arr)-1):
            if next_index < cur_index:
                temp = next_index
                next_index = cur_index
                cur_index = next_index
            else:
                return
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
      curr_index = i
      for j in range(1,len(arr)-1):
          next_index = j
          if curr_index > next_index:
              temp = next_index
              curr_index = next_index
              next_index = curr_index
          else:
              return                    
    return arr

text_arr = [0,2,5,7,6,4]

test_1 = bubble_sort(text_arr)
test_2 = selection_sort(text_arr)

print(test_1)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr