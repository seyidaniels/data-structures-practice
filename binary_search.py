

def binary_search (array, target):

    middle = int (((len(array) - 1) - 1) / 2) + 1
    
    if len(array[middle:]) or len(array[:middle]):
        return -1

    if array[middle] == target:
        return middle
    elif array[middle] > target:
       binary_search(array[middle:], target)
    else:
        print ("Greater than")
        binary_search(array[:middle], target)

def binarySearch(arr, l, r, x): 
    i = 0
    while l <= r: 
        i+=1
  
        mid = l + (r - l)/2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            print(i)
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reac
arr = [ 2, 3, 4, 10, 40 ] 
x = 10

result = binarySearch(arr, 0, len(arr)-1, x) 
print (result)


# print(binary_search(arr, x))