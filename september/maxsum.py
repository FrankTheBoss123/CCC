def maxsum(array):
    biggest = [0]*len(array)
    for x in range(len(array)):
        if x-1 > 0:
            for y in range(0,x-1):
                biggest[x] = max(biggest[x],array[x]+biggest[y])
        else:
            biggest[x] = max(biggest[x],array[x])
    ans = 0
    for num in biggest:
        ans = max(num,ans)
    return ans

print(maxsum([75,105,120,75,90,135]))
