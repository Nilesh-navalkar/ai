#functions of nltk: -stemming  -levitization

#Stemming is a process of normalization, in which words are reduced to their root word (or) stem
#Stemming is a technique used to extract the base form of the words by removing affixes from them. 
#It is just like cutting down the branches of a tree to its stems. For example, the stem of the words eating, eats, eaten is eat.

#lemmatization is also used to reduce the word to their root word. Lemmatizing gives the complete meaning of the word which makes sense.
#It uses vocabulary and morphological analysis to transform a word into a root word.
#The output we will get after lemmatization is called ‘lemma’, which is a root word rather than root stem, the output of stemming. 
#After lemmatization, we will be getting a valid word that means the same thing.

#references :
#[1] https://www.analyticsvidhya.com/blog/2021/07/getting-started-with-nlp-using-nltk-library/
#[2] https://www.tutorialspoint.com/natural_language_toolkit/natural_language_toolkit_stemming_lemmatization.html

from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer

def stemming(words):
    print("#Stemming is a process of normalization, in which words are reduced to their root word (or) stem : ")
    print("stemming words : ",words)
    snow_stem = SnowballStemmer(language='english')
    for word in words:
        print(word + '--->' + snow_stem.stem(word))

def lemminization(tokenized_word):
    print("lemmatization is also used to reduce the word to their root word. Lemmatizing gives the complete meaning of the word which makes sense.It uses vocabulary and morphological analysis to transform a word into a root word. ")
    print("lemminization words : ",tokenized_word)
    lemmatizer = WordNetLemmatizer()
    lemmatized_words_list = []
    for each_word in tokenized_word:
        lem_word = lemmatizer.lemmatize(each_word)
        lemmatized_words_list.append(lem_word)
    print('Text with Stop Words: {}'.format(tokenized_word))
    print('Lemmatized Words list {}'.format(lemmatized_words_list))


words = ['happy', 'happier', 'happiest', 'happiness', 'breathing','fairly','eating']
#stemming(words)
txt="Life will always have problems and pressures."
lemminization(txt.split())