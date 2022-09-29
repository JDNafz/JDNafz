def dijkstrasAlgorithm(start, edges):
  unvisited = [*range(len(edges))]
  nodeDistance = [float("inf") for _ in edges]
  nodeDistance[start] = 0
  neighbors = []
  current = start

  while unvisited:
    currAdjList = edges[current]
    currNeighbors = [[idx, dist] for [idx, dist] in currAdjList]
    print("currNeigh:",currNeighbors)
    #revisit later
    unvisitedNeighbors = [[idx, dist] for [idx, dist] in currNeighbors if idx in unvisited]
    print("unvisitedNeigh:", unvisitedNeighbors)
    for neighbor in unvisitedNeighbors:
      tentativeValue = neighbor[1] + nodeDistance[current]
      nodeDistance[neighbor[0]] = min(tentativeValue, nodeDistance[neighbor[0]])
    unvisited.remove(current)
         
    current = selectCurrent(unvisited, nodeDistance)
    if nodeDistance[current] == float('inf'):
      break

  output = [-1 if distance == float('inf') else distance for distance in nodeDistance ]

  # for idx in range(len(nodeDistance)):
  #   if nodeDistance[idx] == float('inf'):
  #     nodeDistance[idx] = -1
  return output

  # for distance in nodeDistance:
  #   if distance == float('inf'):
  #     output.append(-1)
  #   else:
  #     output.append(distance)

  

def selectCurrent(unvisited,nodeDistance):
  considerVerticies = []
  for vertex in unvisited:
    considerVerticies.append(nodeDistance[vertex])
  minDistance = min(considerVerticies)
  current = nodeDistance.index(minDistance)
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
dijkstrasAlgorithm(0,array)
