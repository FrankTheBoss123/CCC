
def subarraysort(array):
    start = -1
    end = -1
    for x in range(len(array)):
        if array[x]!=min(array[x:]):
            start = x
            break
    for x in range(len(array)-1,-1,-1):
        if array[x]!=max(array[:x+1]):
            end = x
            break
    return [start,end]

print(subarraysort([1,2,3,7,10,11,7,12,6,7,16,18,19]))
