import statespace


initial=[[1,2,3],[-1,4,6],[7,5,8]]
final=[[1,2,3],[4,5,6],[7,8,-1]]


#print(s_space)
visited = set() 

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

graph=statespace.move(initial,final)

print("traversal : ")
dfs(visited,graph,0)