import pyttsx3 

s = pyttsx3.init()
doc="this.txt"
with open(doc, 'r', encoding='utf-8') as f:
    read_data = f.read()


s.say(read_data)
s.runAndWait()