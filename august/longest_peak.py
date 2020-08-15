array = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]

peaks = []

for x in range(1,len(array)-1):
    if array[x-1] < array[x] > array[x+1]:
        peaks.append(x)

longest = 0
for peak in peaks:
    j = peak
    num = 0
    while array[j-1] < array[j] and j > 0:
        num+=1
        j-=1
    j = peak
    while array[j] > array[j+1] and j < len(array)-1:
        num+=1
        j+=1
    longest = max(num,longest)

print(longest)
