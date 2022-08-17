'''

https://www.algoexpert.io/questions/sorted-squared-array

🟢 Easy Difficulty
'''

# O(n log(n)) time | O(n) Space
def sortedSquaredArray(array):
    targetArray= [];
    for i in range(len(array)):
        targetArray.append(array[i]**2 );
    targetArray.sort();
    return targetArray
