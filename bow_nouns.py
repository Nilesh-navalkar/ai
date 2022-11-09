import nltk

def get(sentence):
    t=[]
    tokenized_word = sentence.split()
    need=nltk.pos_tag(tokenized_word, tagset='universal')
    for i in range(0,len(need)):
        if(need[i][1]=="NOUN"):
            t.append(need[i][0])

    return t

n=int(input("enter number of sentences to build vocabulary : "))
sentences=[]
for i in range(0,n):
    l=input()
    sentences.append(l)

vocab=set()
for i in sentences:
    t=get(i)
    for k in t:
        vocab.add(k)

print("vocab : ",vocab)
print("sentences : ",sentences)
voclist=list(vocab)
bow=[]
for i in sentences:
    vi=[]
    for m in range(0,len(vocab)):
        vi.append(0)

    l=i.split()
    for i in range(0,len(vi)):
        if voclist[i] in l:
            vi[i]=vi[i]+1

    bow.append(vi)

print("bag of words : ")
print(bow)
