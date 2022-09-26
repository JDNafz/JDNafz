'''
sort tasks to be assigned to number of workers(k) 
so that everyone finishes as fast as possible.

🔵 Medium
https://www.algoexpert.io/questions/task-assignment
'''

def taskAssignment(k, tasks):


    sortedTasks = sorted(list(enumerate(tasks)), key = lambda x: x[1])
    # print(sortedTasks)
    assignedTasks = []
    for i in range(k):
        endPointer = len(tasks) -1 - i
        #zero represents the location of the idx from the inital array, a 1 would represent 
        # the value in hours of the task that needs to be completed.
        assignedTasks.append((sortedTasks[i][0],sortedTasks[endPointer][0]))
    print(assignedTasks)
    return assignedTasks

taskAssignment(3,[1, 3, 5, 3, 1, 4])






'''

# This is all thinking through the first expression in the function
# play with print statements to figure things out
    
    # "lambda" is an anonymous function instead I played with writing a function called "lambada" (like the dance)
    #to see exactly what lambda is doing in this example.
    def lambada(enumeratedTuple):
        #this returns the hour value 
        return enumeratedTuple[1]
        return enumeratedTuple[0] # this would return the enumerated idx

    
    sortedTasks2 = sorted(list(enumerate(tasks)), key = lambada)
    
    print(tasks)
    # >> [1, 3, 5, 3, 1, 4]
    
    enumeratedTasks = list(enumerate(tasks))
    # >> [(0, 1), (1, 3), (2, 5), (3, 3), (4, 1), (5, 4)]
    # (Enumerated Idx, tasks length)

    sortedTasks3 = sorted([(0, 1), (1, 3), (2, 5), (3, 3), (4, 1), (5, 4)],key = lambada)
    # print(enumeratedTasks)
    # print(sortedTasks3)

    '''

