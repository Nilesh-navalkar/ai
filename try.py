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
    n=[]
    for i in neighbours:
        ele=i.split(",")
        n.append((ele[0],int(ele[1])))
    graph[state]=n

print(graph)