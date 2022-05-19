def linear_search(arr, n):
    for i in range (len(arr)):
        if arr[i]==n:
            return i
    return -1

arr=[2,6,1,255,3,8,16,12,21,33,32,35,100,51,44]
n=int(input("Enter a search element: "))
search_element=linear_search(arr, n)
#print(search_element)

if search_element != -1:
    print("Element is present at index", str(search_element))
else:
    print("Element is not present in array")