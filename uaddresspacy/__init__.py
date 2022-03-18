import spacy
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
##
# PARSE
#
def parse(raw):
    nlp = spacy.load('models/model-best')
    doc = nlp(improver.improve_address(raw.lower()))

    return [(ent.text, ent.label_) for ent in doc.ents]
