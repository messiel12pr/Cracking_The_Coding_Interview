# There are three types of edits that can be performed on strings: insert a char,
# remove a char, or replace a char. Given two strings, write a function to 
# check if they are one edit (or zero edits) away.

def one_away(str_1: str, str_2: str) -> bool:
    if abs(len(str_1) - len(str_2)) > 1:
        return False
    
    ptr_1 = ptr_2 = 0
    flag = False

    while ptr_1 < max(len(str_1), len(str_2))-1 and ptr_1 < max(len(str_1), len(str_2))-1:
        if flag == True and str_1[ptr_1] != str_2[ptr_2]:
            return False
        
        if str_1[ptr_1] == str_2[ptr_2]:
            ptr_1 += 1
            ptr_2 += 1

        elif str_1[ptr_1] != str_2[ptr_2] and flag != True:
            if len(str_1) == len(str_2):
                ptr_1 += 1
                ptr_2 += 1
                flag = True

            elif len(str_1) < len(str_2):
                ptr_1 += 1
                ptr_2 += 2
                flag = True

            elif len(str_1) > len(str_2):
                ptr_1 += 2
                ptr_2 += 1            
                flag = True

    return True

print("pale, ple " + str(one_away('pale', 'ple')))
print("pales, pale " + str(one_away('pales', 'pale')))
print("pale, bale " + str(one_away('pale', 'bale')))
print("pale, bake " + str(one_away('pale', 'bake')))