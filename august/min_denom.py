target = 7
denoms = [1,5,10]
ways = [0]+[float("inf")]*target

for denom in denoms:
    for index in range(denom,target+1):
        ways[index] = min(ways[index-denom]+1,ways[index])

print(f"min answer: {ways[target]}")
