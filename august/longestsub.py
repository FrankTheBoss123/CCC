

def longestString(input):
    longest = ""
    num = 0
    for char in input:
        temp = get_longest_possible(input[num:])
        if len(temp) > len(longest):
            longest = temp
        num+=1
    return longest

def get_longest_possible(input):
    list = []
    temp = ""
    for character in input:
        if character not in list:
            list.append(character)
            temp+=character
        else:
            return temp
    return temp

print(longestString("clementisacap"))
