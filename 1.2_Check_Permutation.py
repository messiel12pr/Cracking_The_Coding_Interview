# Given two strings, write a method to decide if one is a permutation of the other

# O(n) approach
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

str_1 = 'the cat in the hat @ 123!'
str_2 = '!321 @ tah eht ni tac eht'

print('Are ' + str_1 + ' and ' + str_2 + ' permutations? ' + str(check_permutation(str_1, str_2)))

str_1 = 'Hello World@'
str_2 = 'Hello World!'

print('Are ' + str_1 + ' and ' + str_2 + ' permutations? ' + str(check_permutation(str_1, str_2)))