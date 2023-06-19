# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structurs?

# O(n log(n)) Time Complexity, O(1) Space Complexity approach

def is_Unique(str_1: str) -> bool:
    str_1 = sorted(str_1)

    for i in range(len(str_1)-1):
        if str_1[i] == str_1[i+1]:
            return False
        
    return True

str_unique = 'asdfghjkl12345@#$%^& _[]'
str_not_unique = 'asdfghhjkl12345@#$%^& _[]'

print('Is String: ' + str_unique + ' Unique? ' + str(is_Unique(str_unique)))
print('Is String: ' + str_not_unique + ' Unique? ' + str(is_Unique(str_not_unique)))