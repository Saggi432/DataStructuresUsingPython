
def binary_search(input_array, value):
    length = len(input_array)
    low=0
    high=length-1
  
  
    while low <= high:
        mid = (low+high)/2
        if input_array[mid] == value:
            return mid
        if value > input_array[mid]:
            low=mid+1
        else:
            high=mid-1
            


