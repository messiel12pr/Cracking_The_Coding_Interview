# Given two strings, write a method to decide if one is a permutation of the other

def check_permutation(str_1: str, str_2: str) -> bool:
    arr = [0] * 128

    if len(str_1) != len(str_2):
        return False

    for i in range(len(str_1)):
        arr[ord(str_1[i])] += 1

    for i in range(len(str_2)):
        arr[ord(str_2[i])] += -1
        if arr[ord(str_2[i])] < 0:
            return False
        
    return True

str_1 = 'hola mi pana'
str_2 = 'anap im aloh'

print(check_permutation(str_1, str_2))