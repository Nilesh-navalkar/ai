'''
graph={"s":["b","c"] , "b":["c","d","g","s"] , "c":["e","f","g","s","b"] , "d":["g","b"] , "e":["c"], "f":["c"], "g":["b","c","d"]}
h={"s":11,"b":2,"c":4,"d":6,"e":4,"f":1,"g":0}
'''
graph={}
h={}
n=int(input("enter the number of states : "))
for i in range(0,n):
    state=input("enter the state : ")
    huristic=int(input("enter the heurixtic of current state : "))
    h[state]=huristic
    n_line=input("enter the neighbours: ")
    neighbours=n_line.split()
    graph[state]=neighbours


def traversal(path,graph,h):
    if(path[-1]=="g"):
        print("search complete goal reached : ",path)
        return
    elif len(graph[path[-1]])==0:
        print("search terminated at :",path)
        return
    else:
        min=(h[graph[path[-1]][0]],graph[path[-1]][0])
        for i in graph[path[-1]]:
            if(h[i]<min[0]):
                min=(h[i],i)
        return traversal(path+min[1],graph,h)        

traversal("s",graph,h)
