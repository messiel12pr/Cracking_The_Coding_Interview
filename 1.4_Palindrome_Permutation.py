# Given a string, write a function to check if it is a permutation of a palindrome.
# Ignore case and non-letter chars

def palindrome_permutation(str_1: str) -> bool:
    hm = {}
    for i in range(len(str_1)):
        if str_1[i].lower() not in hm:
            hm[str_1[i].lower()] = 1

        else:
            hm[str_1[i].lower()] = hm[str_1[i].lower()] + 1
    
    even = 0
    for i in hm.values():
        if i%2 != 0:
            even = even + 1
        
        if even > 1:
            return False
        
    return True

print("tactCoa is a palindrome permutation " + str(palindrome_permutation('tactCoa')))
print("Tacocat is a palindrome permutation " + str(palindrome_permutation('Tacocat')))
print("notPalindromePerm is a palindrome permutation " + str(palindrome_permutation('notPalindromePerm')))