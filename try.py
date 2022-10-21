
color={"1":1,"2":0,"3":2}
a= sorted(color.items(), key=lambda x: x[1])
color={}
for i in a:
    color[i[0]]=i[1]

print(color)