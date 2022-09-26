'''
Calculate the distance+mpg to see if you can get to the next city. 

🔵 Medium
https://www.algoexpert.io/questions/valid-starting-city
'''

def validStartingCity(distances, fuel, mpg):
    currentTank, startingCity = 0, 0
    for i in range(len(distances)):
        fuelMiles = fuel[i] * mpg
        currentTank += fuelMiles 
        currentTank -= distances[i]
        # print("currTank after driving to city:",currentTank)
        if currentTank < 0:
            startingCity = i+1
            currentTank = 0
            # print("StartingCity can't be",i,"so starting city is:",startingCity)
    # print(startingCity)
    return startingCity







# distances = [5, 25, 15, 10, 15]
# fuel =      [1,  2,  1,  0,  3]
# mpg = 10

# distances =  [10, 20, 10, 15, 5, 15, 25]
# fuel =       [ 0,  2,  1,  0, 0,  1,  1]
# mpg =  20

# distances = [1, 3, 10, 6, 7, 7, 2, 4]
# fuel =      [1, 1,  1, 1, 1, 1, 1, 1]
# mpg = 5
#should be 6

distances = [30, 40, 10, 10, 17, 13, 50, 30, 10, 40]
fuel =      [ 1,  2, 0, 1, 1, 0, 3, 1, 0, 1]
mpg = 25
  #should be 1

validStartingCity(distances,fuel,mpg)