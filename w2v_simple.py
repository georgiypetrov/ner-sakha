import gensim
import numpy as np
import pandas as pd
from catboost import CatBoostClassifier
from sklearn.metrics import classification_report

model = gensim.models.KeyedVectors.load_word2vec_format('all.bin', binary=True)


def read_data(file):
    with open(file) as f:
        sentences = [sentence.split('\n') for sentence in f.read().split('\n\n')]
        df = pd.DataFrame([line.split() for sentence in sentences for line in sentence], columns=['word', 'tag'])
    return df


def get_embedding(word):
    try:
        return model.get_vector(word.lower()).tolist()
    except KeyError:
        return np.zeros(150).tolist()


train = read_data('data/collection_3/train.txt')
test = read_data('data/collection_3/test.txt')

train['emb'] = train['word'].apply(lambda x: get_embedding(x))
test['emb'] = test['word'].apply(lambda x: get_embedding(x))

clf = CatBoostClassifier(iterations=500, learning_rate=0.8, depth=7)
clf.fit(train['emb'], train['tag'])
print(classification_report(test['tag'], clf.predict(test['emb'])))
