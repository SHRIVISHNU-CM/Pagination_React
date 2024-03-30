#function definition
def depthFirstTraversal(visited , graph, node):
    if node not in visited:
        print(node, end = " ")
        visited.add(node)
        for adjacentNodes in graph[node]:
            if adjacentNodes not in visited:
                depthFirstTraversal(visited, graph, adjacentNodes)



#driver code
visited = set()

graph = {
    '5':['3', '7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}

#function calling
depthFirstTraversal(visited, graph, '5')