import json
from collections import defaultdict
import spacy

def getResumeData(doc):
    data = defaultdict(list)
    for ent in doc.ents:
        label = ent.label_.lower()
        print(label)
        print(ent.label_)
        data[label].append(ent.text)
        data[label] = list(set(data[label]))
    return json.dumps(data, indent=4)

def processText(text):
    nlp_ner = spacy.load("output/model-best") 
    doc = nlp_ner(text)
    return getResumeData(doc)

