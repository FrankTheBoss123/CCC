def encrypt(string,num):
    ans = ""
    for char in string:
        newnum = (ord(char)-97+num)%26
        ans+=chr(newnum+97)
    return ans

print(encrypt("xyz",2))
