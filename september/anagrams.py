def get_anagrams(array):
    dict = {}
    for string in array:
        newstring = ''.join(sorted(string))
        if newstring in dict:
            dict[newstring].append(string)
        else:
            dict[newstring] = [string]
    return list(dict.values())

array = ["yo","act","flop","tac","foo","cat","oy","olfp"]
print(get_anagrams(array))
