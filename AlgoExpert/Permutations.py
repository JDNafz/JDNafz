#Upper Bound O(n^2*n!) time | O(n*n) space

# def getPermutations(array):
#     perms = []
#     helper(array,[],perms)
#     print(perms)
#     return perms


# def helper(array,perm, perms):
#     if not len(array) and len(perm):
#         perms.append(perm)
#     else:
#         for i in range(array):
#             newArray  = array[:i] + array[i + 1:]
#             newPerm = perm + [array[i]]
#             helper(newArray,newPerm,perms)
#     return perms

# getPermutations([1,2,3])

def getPermutations(array):
    perms = []
    helper(0,array,perms)
    print(perms)
    return perms


def helper(i, array, perms):
    if i = len(array) - 1:
        perms.append(array[:])
    else:
        for j in range (i, len(array)):
            swap(array,i,j):
            helper(i + 1, array, perms)
            swap(array, i, j)


    return perms

def swap(array,i,j):
    array[i], array[j] = array[j], array[i]



getPermutations([1,2,3])