'''
Without using division find the product of all 
other elements in the array, add the product to the output array.

🔵 Medium Difficulty

https://www.algoexpert.io/questions/array-of-products
'''
def arrayOfProducts(array):
    # Write your code here.

    products = [1 for _ in array]
    runningProduct = 1
    for i in range(len(array)):
        products[i] = runningProduct
        runningProduct *= array[i]
    
    runningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= runningProduct
        runningProduct *= array[i]

    print(products)
    return products



arrayOfProducts([5, 1, 4, 2])
# [8, 40, 10, 20]