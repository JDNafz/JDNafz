# 🔵 Medium
#really need to review this solution again, but it's working.

def getPermutations(array):
    perms = []
    helper(0,array,perms)
    print(perms)
    return perms


def helper(i, array, perms):
    if i == len(array) - 1:
        perms.append(array[:])
    else:
        for j in range (i, len(array)):
            swap(array,i,j)
            helper(i + 1, array, perms)
            swap(array, i, j)


    return perms

def swap(array,i,j):
    array[i], array[j] = array[j], array[i]



getPermutations([1,2,3])