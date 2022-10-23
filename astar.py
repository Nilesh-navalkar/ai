#graph={"s":[("b",3),("c",4)] , "b":[("c",1),("d",2),("g",3),("s",3)] , "c":[("e",1),("f",3),("g",4),("s",4),("b",1)] , "d":[("g",1),("b",2)] , "e":[("c",1)], "f":[("c",3)], "g":[("b",3),("c",4),("d",1)]}
#h={"s":11,"b":2,"c":4,"d":6,"e":4,"f":1,"g":0}

graph={}
h={}
n=int(input("enter the number of states : "))
for i in range(0,n):
    state=input("enter the state : ")
    huristic=int(input("enter the heurixtic of current state : "))
    h[state]=huristic
    n_line=input("enter the neighbours,distance of neighbour : ")
    neighbours=n_line.split()
    ni=[]
    for i in neighbours:
        ele=i.split(",")
        ni.append((ele[0],int(ele[1])))
    graph[state]=ni


q=[]
def dq(q):
    top=q[0]
    del q[0]
    return top[0]

def calculatefx(top,h,graph):
    f=0
    for i in range(1,len(top),1):
        n1=graph[top[i-1]]
        for j in n1:
            if(top[i]==j[0]):
                f=f+j[1]
    
    return f+h[top[-1]]

def removecycle(q):
    cycli=[]
    for i in range(0,len(q)):
        if(len(q[i][0])!=len(set(q[i][0]))):
            print("removing cycle " ,q[i])
            cycli.append(q[i])
    for i in cycli:
        del q[q.index(i)]        
    print("--> ",q)

def removeoverlap(q):
    olapi=[]
    for i in range(0,len(q)-1):
        for j in range(i+1,len(q)):
            if(q[i][0][0]==q[j][0][0] and q[i][0][-1]==q[j][0][-1]):
                print("removing overlap " ,q[j])
                olapi.append(q[j])
    for i in olapi:
        del q[q.index(i)]
    print("--> ",q)

def traverse(graph,h):
    q.append(("s",h["s"]))
    #print(q)
    #print(q[0][0])
    
    while(True):
        top=dq(q)
        #print("top ",top)
        n=graph[top[-1]]
        for i in n:
            f=calculatefx(top+i[0],h,graph)
            q.append((top+i[0],f))
        q.sort(key = lambda x: x[1])
        print("--> ",q)
        removecycle(q)
        removeoverlap(q)
        if(q[0][0][-1]=="g"):
            return q[0]


print(traverse(graph,h))