from nltk import word_tokenize
import nltk
from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
text = 'Learn to lose your destiny to find where it leads you'
filtered_text = []
tokenized_word = word_tokenize(text)
for each_word in tokenized_word:
    if each_word not in stop_words:
        filtered_text.append(each_word)
print('Toxenized list with stop words: {}'.format(tokenized_word))
print('Toxenized list with out stop words: {}'.format(filtered_text))