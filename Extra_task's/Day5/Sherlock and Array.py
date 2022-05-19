def balancedSums(arr):
    # Write your code here
    right_arr=sum(arr)
    left_arr=0
    for i in arr:
        right_arr=right_arr-i
        if left_arr==right_arr:
            return "YES"
        left_arr=left_arr+i
    
    return "NO"