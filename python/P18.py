from collections import deque
queue = deque()

def breadthFirstTraversal(visited, graph ,node):
    visited.add(node)
    queue.appendleft(node)

    while queue:
        node = queue.pop()
        print(node, end = ' ')
        for adjacentNode in graph[node]:
            if adjacentNode not in visited:
                visited.add(adjacentNode)
                queue.appendleft(adjacentNode)


#driver code
visited =set()
graph = {
    'a' :['b','c','d'],
    'b':['e'],
    'c':['e', 'f'],
    'd':['f'],
    'e':['g'],
    'f':['g'],
    'g':[]
}

breadthFirstTraversal(visited,graph,'a' )