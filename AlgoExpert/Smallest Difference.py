'''
https://www.algoexpert.io/questions/smallest-difference

🔵 Medium Difficulty

'''


def smallestDifference(arrayOne, arrayTwo):
    #start at 2:58PM
    arrayOne.sort()
    arrayTwo.sort()
    print(arrayOne, arrayTwo)
    i = 0 
    j = 0
    smalldif = abs(arrayOne[0] - arrayTwo[0])
    while i < len(arrayOne) and j < len(arrayTwo):
        if abs(arrayOne[i] - arrayTwo[j]) == 0:
            small_i = i
            small_j = j
            break
        if abs(arrayOne[i] - arrayTwo[j]) <= smalldif:
            smalldif = abs(arrayOne[i] - arrayTwo[j])
            small_i = i
            small_j = j 
        if arrayOne[i] < arrayTwo[j]:
            i += 1   
        else:
            j += 1;
        
  
    return [arrayOne[small_i], arrayTwo[small_j]]

    
