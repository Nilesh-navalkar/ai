from sklearn.feature_extraction.text import TfidfVectorizer

d0 = 'hello world'
d1 = 'hell you world'
d2 = 'hello from the otherside of world'

corpus = [d0, d1, d2]

tfidf = TfidfVectorizer()
result = tfidf.fit_transform(corpus)


print('\nWord indexes:')
print(tfidf.vocabulary_)
print('\ntf-idf value:')
print(result)
print('\ntf-idf values in matrix form:')
print(result.toarray())
