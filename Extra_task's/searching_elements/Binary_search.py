def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
            
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1

arr = [ 2, 3, 4, 10, 40, 50, 100, 151, 201, 202, 300]
n=int(input("Enter a search element: "))
search_element=binary_search(arr, 0, len(arr)-1, n)
#print(search_element)

if search_element != -1:
    print("Element is present at index", str(search_element))
else:
    print("Element is not present in array", str(search_element))