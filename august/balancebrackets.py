
dict = {"{":"}","[":"]","(":")"}


def balanced(input):
    queue = []
    for char in input:
        if open(char):
            queue.append(char)
        else:
            if opposite(queue.pop(-1)) != char:
                return False
    if len(queue) != 0:
        return False
    return True

def open(input):
    if input in dict.keys():
        return True
    return False

def opposite(input):
    return dict[input]

print(balanced("{{}{}{}()"))
