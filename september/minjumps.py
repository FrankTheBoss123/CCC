def minjumps(array):
    shortest = [0]+[float("inf")]*(len(array)-1)
    for x in range(len(array)):
        for y in range(1,array[x]+1):
            if x+y < len(array):
                shortest[x+y] = min(shortest[x+y],shortest[x]+1)
    return shortest[-1]

print(minjumps([3,4,2,1,2,3,7,1,1,1,3]))
