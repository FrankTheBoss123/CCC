
def powerset(list):
    ans = [[]]
    for num in list:
        answer = ans.copy()
        for var in answer:
            variable = var.copy()
            variable.append(num)
            ans.append(variable)
    return ans

answer = powerset([1,2,3])
print(answer)
