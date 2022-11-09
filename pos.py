import nltk

text = "I am going to meet M.S. Dhoni."
tokenized_word = text.split()
print(nltk.pos_tag(tokenized_word, tagset='universal'))

