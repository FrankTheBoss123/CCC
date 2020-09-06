def longestsequence(string1,string2):
    string1 = list(dict.fromkeys(sorted(string1)))
    string2 = list(dict.fromkeys(sorted(string2)))
    ans = []
    for val in string1:
        if val in string2:
            ans.append(val)
    return ans

print(longestsequence("zxvvyzw","xkykzpw"))
