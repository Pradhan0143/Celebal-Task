def sortarry(start,end,arr):
    subarry = arr[start:end+1]
    subarry.sort()
    return addElement(arr,subarry)

def addElement(orgArry,subArry):
    for i in orgArry:
        if i in subArry:
            continue
        else:
            ind = orgArry.index(i)
            subArry.insert(ind,i)
    return subArry

def sortedSubsegments(k, a, queries):
    # Write your code here
    arry = a
    for i in range(len(queries)):
        start = queries[i][0]
        end = queries[i][-1]
        arry=sortarry(start,end,arry)
    return arry[k]   
