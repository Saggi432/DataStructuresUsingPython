
def binary_search(input_array, value):
    length = len(input_array)
    low=0
    high=length-1
    mid=(low+high)/2
  
    while low <= high:
        mid = low+high/2
        if value > input_array[mid]:
            low=mid+1
    
        elif input_array[mid] == value:
            return mid

        else value < input_array[mid]:
            high=mid-1
            


