White - Unvisited  0
Grey  - InStack    1
Black - Finished   2


def cycleInGraph(edges):
    visited = [0 for _ in edges]

    for vertex in range(len(edges)):
        if visited[vertex] != 0:
            continue

        traverse(vertex,edges,visited)
        visited[vertex] = 2
        print("its in the stack....")
    return False

def traverse(vertex,edges,visited):
    visited[vertex] = 1
    for i in range(len(edges[vertex])):
        if visited[i] == 2: 
            continue
        if visited[i] == 0:
            traverse(i,edges,visited)
        else: # i = 1



cycleInGraph([
  [1, 3],    # 0
  [2, 3, 4], # 1
  [0],       # 2
  [],        # 3
  [2, 5],    # 4
  []         # 5
])