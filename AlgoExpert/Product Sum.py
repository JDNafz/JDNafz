'''
Sum the array, if the array contains an array, 
multiply the inner array by the depth before summing.

🟢 Easy Difficulty
https://www.algoexpert.io/questions/product-sum
'''
def productSum(array,multiplyer=1):
    # Write your code here.
    totalSum = 0
    for element in array:
        if type(element) == list:
            totalSum += productSum(element, multiplyer+1)
        else:
            totalSum += element
    return totalSum * multiplyer        


spicy = [5,2,[7,-1],3,[6,[-13,8],4]]
productSum(spicy)