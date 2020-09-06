def interweaving(string1,string2,string3):
    if len(string3) == 0:
        return True
    for char in string3:
        if len(string1)!=0 and len(string2)!=0 and string1[0] == string2[0] and char == string1[0]:
            return interweaving(string1,string2[1:len(string2)],string3[1:len(string3)]) or interweaving(string1[1:len(string1)],string2,string3[1:len(string3)])
        elif len(string2)!=0 and string2[0] == char:
            return interweaving(string1,string2[1:len(string2)],string3[1:len(string3)])
        elif len(string1)!=0 and string1[0] == char:
            return interweaving(string1[1:len(string1)],string2,string3[1:len(string3)])
        else:
            return False

print(interweaving(list("abc"),list("123"),list("a1b2c3")))
