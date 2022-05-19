def lilysHomework(arr):
    def no_of_swap(arr):
        indexmap={}
        
        for i in range (len(arr)):
            indexmap[arr[i]]=i
            
        sorted_arr=sorted(arr)
        result=0
        
        for i in range (len(arr)):
            if arr[i] != sorted_arr[i]:
                result += 1
                
                #swap element index
                swap_index=indexmap[sorted_arr[i]]
                #updating swaping index
                indexmap[arr[i]]=swap_index
                #swap opration
                arr[i], arr[swap_index] = arr[swap_index], arr[i]
                
        return result
    
    normal_order=no_of_swap(arr[::])
    revers_order=no_of_swap(arr[::-1])
    
    return min(normal_order, revers_order)