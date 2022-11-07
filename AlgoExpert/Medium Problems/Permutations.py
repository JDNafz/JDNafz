def getPermutations(array):
    return permSearch(array,0,[])
    return array

def permSearch(array,perm, output):
    if not array:
        output.append(perm)
        return
    for _ in range(len(array)):
        newArray = array
        perm = newArray.pop()
        permSearch(newArray, perm, output)
    print(array)
    return array



getPermutations([1,2,3])

# remove(3, [1,2,3,4])


