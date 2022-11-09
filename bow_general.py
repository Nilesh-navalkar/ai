n=int(input("Enter number of sentence to build vocabulary : "))
sentences = []
for i in range(0,n):
    l=input()
    sentences.append(l)

vocab = set()
for i in sentences:
    for j in i.split():
        vocab.add(j)

print("vocab: ",vocab)
print("sentence: ",sentences)
voclist = list(vocab)
bow=[]
for i in sentences:
    vi=[]
    for k in range(0,len(vocab)):
        vi.append(0)

    l=i.split()
    for j in range(0,len(vi)):
        if voclist[j] in l:
            vi[j] = vi[j]+1
        
    bow.append(vi)
print("bag of words: ",bow)
