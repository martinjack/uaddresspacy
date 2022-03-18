import spacy
from spacy.tokens import DocBin
import pandas as pd
import json
import ast

labels = [
    'Country',
    'RegionType',
    'Region',
    'CountyType',
    'County',
    'Included',
    'LocalityType',
    'Locality',
    'StreetType',
    'Street',
    'HousingType',
    'Housing',
    'HostelType',
    'Hostel',
    'HouseNumberType',
    'HouseNumber',
    'HouseNumberAdditionally',
    'SectionType',
    'Section',
    'ApartmentType',
    'Apartment',
    'RoomType',
    'Room',
    'Sector',
    'FloorType',
    'Floor',
    'PostCode',
    'Manually',
    'NotAddress',
    'Comment',
    'AdditionalData'
]

## Init NLP
nlp = spacy.blank('uk')
##

data = pd.read_csv('training/pretrain.csv', sep=";")
db = DocBin()

for name, data in data.iterrows():
    doc = nlp(data['Raw'].lower())
    ents = []
    for item in labels:
        if str(data[item]) == 'nan':
            pass
        else:
            positions = ast.literal_eval(data[item])
            if len(positions) > 1:
                positions = [{'start': positions[0]['start'], 'end': positions[-1]['end']}]
            
            for key, position in enumerate(positions):
                string = doc.char_span(int(position['start']), int(position['end']), label=item) 
                ents.append(string)

    print(ents)
    doc.ents = ents
    db.add(doc)

##
# Build raw models
#
db.to_disk('training/train.spacy')
db.to_disk('training/test.spacy')