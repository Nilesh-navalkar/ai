import dls
import sys
import statespace


initial=[[1,2,3],[-1,4,6],[7,5,8]]
final=[[1,2,3],[4,5,6],[7,8,-1]]

graph=statespace.move(initial,final)
deapth=statespace.getdepth(graph)
limit=1
while(True):
    visited=set()
    print("traversal for limit : ",limit)
    dls.dfs(visited,graph,0,limit)
    limit=limit+1
    if 16 in visited:
        sys.exit()
