
def largestrange(array):
    array.sort()
    i, j = 0,0
    largest = 0
    largest_index = [0,0]
    increment = array[1]-array[0]
    for x in range(1,len(array)):
        if increment != array[x]-array[x-1]:
            increment = array[x]-array[x-1]
            if j-i>largest:
                largest_index = [i,j]
                largest = j-i
            i,j = x,x
        else:
            j+=1
    return largest_index

print(largestrange([1,11,3,0,15,5,2,4,10,7,12,6]))
