# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold
# the additional characters, and that you are given the "true"
# length of the string. 

# Example:
# Input:    "Mr John Smith    "
# Output:   "Mr%20John%20Smith"

# O(n) Time Complexity Two Pointer approach
def urlify(str_1: str) -> str:
    r = l = len(str_1)-1
    str_list = list(str_1) 

    while str_list[l] == ' ':
        l -= 1
   
    while l > 0:
        if str_list[l] != ' ':
            str_list[r] = str_list[l]
            l -= 1
            r -= 1

        else:
            l -= 1
            str_list[r] = '0'
            r -= 1
            str_list[r] = '2'
            r -= 1
            str_list[r] = '%'
            r -= 1
    return ''.join(str_list)

str_1 = 'Mr John Smith    '
print('String before URLify: ' + str_1 + ' String after URLify: ' + urlify(str_1))
