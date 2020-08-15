target = 10
denoms = [1,2,5]
ways = [1]+[0]*(target)

for denom in denoms:
    for index in range(denom,target+1):
        ways[index] += ways[index-denom]

print(f"amount of different ways are: {ways[target]}")
