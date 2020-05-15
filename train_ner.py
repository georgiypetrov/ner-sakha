from deeppavlov import train_model

ner_model = train_model('ner.json', download=False)
