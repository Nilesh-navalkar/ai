#given graph colormin
#graph={"a":["b","c"] , "b":["c","a"] , "c":["d","e","a","b"] , "d":["c"] , "e":["c"]}
color={}

graph={}
n=int(input("enter the number of states"))
for i in range(0,n):
    state=input("enter the state : ")
    n_line=input("enter the neighbours : ")
    neighbours=n_line.split()
    graph[state]=neighbours

def sort(color):
    a= sorted(color.items(), key=lambda x: x[1])
    color={}
    for i in a:
        color[i[0]]=i[1]

def colorthis(e):
    color[e]=0
    sort(color)
    for i in  graph[e]:
        if(i not in color.keys()):
            a=0
        elif(color[i]==color[e]):
            color[e]=color[e]+1

def colornode(graph):
    for e in graph.keys():
        colorthis(e)

    print(color)
    #print("given graph can be colored in ",max(color.values)+1 ," colors")

#print(graph.keys())
colornode(graph)