'''
for non-empty array find all 3 number combos that can sum to the target.

🔵 Medium Difficulty
https://www.algoexpert.io/questions/three-number-sum
'''


def threeNumberSum(array, targetSum):
    # Write your code here.

    #return array
    ret = []
    array.sort()

    #check ever index against all future numbers and combinations
    for i in range(len(array)-2):
        #set pointers to compare against i
        left,right = i+1,len(array)-1

        #for the remaining number of possibilties narrow left and right pointers.
        # range(len(array)-2-i): "-2" indicates were using 3 items, can't use more than that, 
        # "-i" because everytime we finish and index, we need to compare against one less
        for _ in range(len(array)-2-i):
            sum = array[i] + array[left] + array[right]
            if sum < targetSum:
                left +=1
            elif sum > targetSum:
                right -=1
            else:
                ret.append([array[i], array[left], array[right]])
                left +=1
    print(ret)
    return ret

threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6],0)