import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
import json

# nlp = spacy.blank("en") # load a new spacy model
nlp = spacy.load("en_core_web_lg")
db = DocBin() # create a DocBin object



f = open('./training_data.json')
TRAIN_DATA = json.load(f)

# for text, annot in tqdm(TRAIN_DATA['entities']): 
#     doc = nlp.make_doc(text) 
#     ents = []
#     for start, end, label in annot["entities"]:
#         span = doc.char_span(start, end, label=label, alignment_mode="contract")
#         if span is None:
#             print("Skipping entity")
#         else:
#             ents.append(span)
#     doc.ents = ents 
#     db.add(doc)

# db.to_disk("./training_data.spacy") # save the docbin object
def resolve_overlaps(entities):
    sorted_entities = sorted(entities, key=lambda x: (x["start_offset"], x["end_offset"]))
    resolved = []
    for ent in sorted_entities:
        if not resolved or ent["start_offset"] >= resolved[-1]["end_offset"]:
            resolved.append(ent)
    return resolved

for item in tqdm(TRAIN_DATA):
    text = item["text"]
    annot = resolve_overlaps(item["entities"])  # Resolve overlaps
    doc = nlp.make_doc(text)
    ents = []
    for entity in annot:
        start = entity["start_offset"]
        end = entity["end_offset"]
        label = entity["label"]
        while start < len(text) and text[start].isspace():
            start += 1
        while end > start and text[end - 1].isspace():
            end -= 1
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print(f"Skipping invalid span: {text[start:end]} ({start}, {end})")
        else:
            ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk("./train.spacy")
