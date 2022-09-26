'''
Check if there's a cycle in the graph


🔵 Medium
https://www.algoexpert.io/questions/cycle-in-graph
'''


# Unvisited  0
# InCycle    1
# Finished   2


def cycleInGraph(edges):
    visited = [0 for _ in edges]

    for vertex in range(len(edges)):
        if visited[vertex] != 0:
            continue

        foundCycle = traverse(vertex,edges,visited)
        if foundCycle:
            print("True")
            return True
    print("False")
    return False

def traverse(vertex,edges,visited):
    print("visited:",visited,"\n",vertex,)
    visited[vertex] = 1
    nextVerts = edges[vertex]
    for vert in nextVerts:
        if visited[vert] == 1: 
            return True
        if visited[vert] == 2:
            continue
        foundCycle = traverse(vert,edges,visited)
        if foundCycle:
            print("True")
            return True
    visited[vertex] = 2
    return False



a = [
  [1, 3],    # 0
  [2, 3, 4], # 1
  [0],       # 2
  [],        # 3
  [2, 5],    # 4
  []         # 5
]
b = [
    [1, 2],
    [2],
    []
  ]

cycleInGraph(b)
