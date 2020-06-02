import fasttext

with open('data/all.txt', encoding='utf8') as f:
    s = f.read()
    s = s.lower()

with open('data/all_lower.txt', 'w', encoding='utf8') as f:
    f.write(s)

model = fasttext.train_unsupervised('data/all_lower.txt', dim=100)
model.save_model('data/emb100.bin')
