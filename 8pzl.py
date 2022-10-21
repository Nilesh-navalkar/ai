import copy
from collections import defaultdict
from treelib import Node, Tree


initial=[[1,2,3],[-1,4,6],[7,5,8]]
final=[[1,2,3],[4,5,6],[7,8,-1]]

tree=defaultdict(list)
graph=defaultdict(list)

def locate(matrix):
    for i,j  in enumerate(matrix):
        if -1 in j:
            index=(i,j.index(-1))
            return index
            
def checkmoves(matrix):
    indx=locate(matrix)
    moves=["u","d","l","r"]
    if(indx[1]==0):
        moves.remove("l")
    if(indx[1]==2):
        moves.remove("r")
    if(indx[0]==0):
        moves.remove("u")
    if(indx[0]==2):
        moves.remove("d")

    return moves

def swap(matrix,i,f):
    temp=matrix[i[0]][i[1]]
    matrix[i[0]][i[1]]=matrix[f[0]][f[1]]
    matrix[f[0]][f[1]]=temp

def move(matrix,final):
    nextlvl=[]
    nextlvl.append(matrix)
    for m in nextlvl:
        p=0
        moves=checkmoves(m)
        indx=locate(m)
        nl=[]
        #print(m)
        for i in moves:
            current=copy.deepcopy(m)
            if i=="u":
                k=indx[0]-1
                j=indx[1]
            elif i=="d":
                k=indx[0]+1
                j=indx[1]
            elif i=="l":
                k=indx[0]
                j=indx[1]-1
            elif i=="r":
                k=indx[0]
                j=indx[1]+1

            swap(current,indx,(k,j))
            nl.append(current)
            if current not in nextlvl:
                nextlvl.append(current)
                #print(current)
                tree[nextlvl.index(m)].append(current)
                graph[nextlvl.index(m)].append(nextlvl.index(current))
       
        if final in nextlvl:
            print("\n*** final configuration achieved at :",nextlvl.index(final)," ***\n")
            return nextlvl

def printstatespace(nextlvl):
    print(graph)
    print(tree)
    #print(nextlvl)
    t=Tree()
    t.create_node(0,0)
    for k in graph:
        for v in graph[k]:
            t.create_node(v,v,parent=k)

    t.show()
'''
    t=Tree()
    t.create_node(0,nextlvl[0])
    for k in graph:
        for v in graph[k]:
            t.create_node(v,nextlvl[v],parent=nextlvl[k])

    t.show()
'''

mxtr=move(initial,final)
printstatespace(mxtr)


