'''
🔴 Hard
https://www.algoexpert.io/questions/dijkstra's-algorithm
'''

def dijkstrasAlgorithm(start, edges):
  unvisited = [*range(len(edges))]
  nodeDistance = [float("inf") for _ in edges]
  nodeDistance[start] = 0
  current = start
  while unvisited:
    currAdjList = edges[current]
    currNeighbors = [[idx, dist] for [idx, dist] in currAdjList]

    #revisit later
    unvisitedNeighbors = [[idx, dist] for [idx, dist] in currNeighbors if idx in unvisited]

    for neighbor in unvisitedNeighbors:
      tentativeValue = neighbor[1] + nodeDistance[current]
      nodeDistance[neighbor[0]] = min(tentativeValue, nodeDistance[neighbor[0]])
    unvisited.remove(current)
 
    current = selectCurrent(unvisited, nodeDistance)
 
    if nodeDistance[current] == float('inf'):
      break
  output = [-1 if distance == float('inf') else distance for distance in nodeDistance ]


  print(output)
  return output

def selectCurrent(unvisited,nodeDistance):
  considerVertices = []
  for vertex in unvisited:
    considerVertices.append(nodeDistance[vertex])
  if not considerVertices:
    return -1 
  minDistance = min(considerVertices)
  considerVertIdx = considerVertices.index(minDistance)
  current = unvisited[considerVertIdx]
  return current


array = [
  [
    [1, 7]
  ],
  [
    [2, 6],
    [3, 20],
    [4, 3]
  ],
  [
    [3, 14]
  ],
  [
    [4, 2]
  ],
  [],
  []
]       
start1= 0
array2 = [[[1, 3],[2, 2]],[[3, 7]],[[1, 2],[3, 4],[4, 1]],[],[[0, 2],[1, 8],[3, 1]]]
start2 = 4
array22 = [0,1,2,3,4,5,6]
array3 = [
    [[1, 1],[3, 1]],
    [[2, 1]],
    [[6, 1]],
    [[1, 3],[2, 4],[4, 2],[5, 3],[6, 5]],
    [[5, 1]],
    [[4, 1]],
    [[5, 2]],
    [[0, 7]]
  ]
start3 = 7
dijkstrasAlgorithm(start3, array3)
