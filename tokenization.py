doc=open("this.txt" , "r")

def tokenizationWords(para):
    print("tokenization by words : ")
    para.replace(".","")
    print(para.split())

def tokenizationSentence(para):
    print("tokenization by sentence: ")
    l=para.split(".")
    l.remove("")
    print(l)

def tokenizationPara(para):
    print("tokenization by para : ")
    l=para.split("\n")
    l.remove("")
    print(l)

#tokenizationWords(doc.read())
#tokenizationSentence(doc.read())
tokenizationPara(doc.read())