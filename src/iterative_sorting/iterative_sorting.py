# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(i + 1,len(arr)):
            next_index = j
            if next_index < cur_index:
                smallest_index = next_index

                temp = arr[cur_index]
                arr[cur_index] = arr[smallest_index]
                arr[smallest_index] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
      curr_index = i
      biggest_index = i
      for j in range(i + 1,len(arr)):
          next_index = j
          if next_index > curr_index:
              biggest_index = next_index
            
              temp = arr[curr_index]
              arr[curr_index] = arr[biggest_index]
              arr[biggest_index] = temp               
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

