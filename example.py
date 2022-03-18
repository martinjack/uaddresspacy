import spacy
import re
import csv
import pandas as pd
import improver

labels = {
    'Raw': '',
    'Country': '',
    'RegionType': '',
    'Region': '',
    'CountyType': '',
    'County': '',
    'Included': '',
    'SubLocalityType': '',
    'SubLocality': '',
    'LocalityType': '',
    'Locality': '',
    'StreetType': '',
    'Street': '',
    'HousingType': '',
    'Housing': '',
    'HostelType': '',
    'Hostel': '',
    'HouseNumberType': '',
    'HouseNumber': '',
    'HouseNumberAdditionally': '',
    'SectionType': '',
    'Section': '',
    'ApartmentType': '',
    'Apartment': '',
    'RoomType': '',
    'Room': '',
    'Sector': '',
    'FloorType': '',
    'Floor': '',
    'PostCode': '',
    'Manually': '',
    'NotAddress': '',
    'Comment': '',
    'AdditionalData': ''
}

nlp = spacy.load('models/model-best')
addresses = pd.read_csv('addresses.csv', sep=';', dtype=str, header=None)


with open('report.csv', 'w') as report:
    writer = csv.writer(report, delimiter=';')
    writer.writerow(labels.keys())

    for index, row in addresses.iterrows():
    
        raw = row[0].lower()
        address = improver.improve_address(raw)

        doc = nlp(address)
        print(address)

        ent_list=[(ent.text, ent.label_) for ent in doc.ents]

        print('Address => ', raw)
        print('NLP => ', str(ent_list))
        print('****')

        for key in labels.keys(): labels[key] = ''

        labels['Raw'] = raw
        print(ent_list)

        for item in ent_list:
            labels[item[1]] = item[0]

        writer.writerow(labels.values())
