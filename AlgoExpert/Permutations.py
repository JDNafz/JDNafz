def getPermutations(array):
    perms = []
    helper(array,[],perms)
    print(perms)
    return perms


def helper(array,perm, perms):
    if len(array) == 0:
        perms.append(perm)
    else:
        for _ in array:
            perm = array.pop()
            helper(array,perm,perms)
    return perms

getPermutations([1,2,3])