
def sort(color):
    a= sorted(color.items(), key=lambda x: x[1])
    color={}
    for i in a:
        color[i[0]]=i[1]
    print(color)
s={"a":1,"b":0}
sort(s)
