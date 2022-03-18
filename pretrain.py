import signal
import threading
import sys
import re
import pandas as pd
import csv
import improver
from os.path import exists

path_pretrain = 'training/pretrain.csv'

labels = [
    'Raw',
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
##
# INTERRUPT
#
def interrupt(signal, frame):
    print('')
    print('#'*50)
    print('Aborting pretrain!')
    sys.exit(0)
##
# SHOW LABELS
#
def show_labels():
   
    print('#' * 50)
    print('Labels')
    print('#' * 50)

    print("| {:<10}| {:<30} |".format('ID', 'NAME'))
    for key, item in enumerate(labels[1:]):
        print("| {:<10}| {:<30} |".format(key+1, item))

##
# READ LIST
#
def read_list():
    data = pd.read_csv('training/raw.csv', sep=";", header=None)
    
    stop = False
    skip = False
    repeat = True
    next_address = False
    ready = 1
    amount = data.index

    for name, item in data.iterrows():
        show_labels()
        address = improver.improve_address(item[0])

        words = re.findall('(?<=\s)\d+\,\s\d+|[a-zA-Zа-яА-ЯіІїЇґҐєЄёЁ0-9.()\/’-№-?]+', address)
        word_pos = []
        pos = 0

        print("#" * 50)
        print("Address ({}/{}): {}".format(ready, len(amount), address))
        print("#" * 50)
        print("|{:<30}| {:<8}| {:<5} |".format('String', 'Start', 'End'))

        data = []

        for i in range(len(words)):
            word = words[i]
            pos += address[pos:].index(word) 
            ##
            regex = re.finditer("^{0}(?=\\s)|(?<=\\s){0}(?=\\s)|(?<=\\s){0}(?=$)|^{0}(?=\\s)".format(improver.str_to_regex(word)), address)
            ##
            if word in words[i+1:] or word in words[:i]:
                word_pos.append(pos) 

                start = pos
                end = start + len(word)
                ##
                duplicate = 0
                for a, b in enumerate(data):
                    if b['string'] == word:
                        duplicate += 1
                ##
                for a, b in enumerate(list(regex)[duplicate:duplicate + 1]):
                    if pos != b.start():
                        start = b.start()
                        end = start + len(word)
                ##
                print("|{:<30}| {:<8}| {:<5} |".format(word, start, end))
                
                data.append({
                    'string': word, 
                    'start': start, 
                    'end': end
                })
            else:
                start = pos
                end = start + len(word)
                ##
                duplicate = 0
                for a, b in enumerate(data):
                    if b['string'] == word:
                        duplicate += 1
                ##
                for a, b in enumerate(list(regex)[duplicate:duplicate + 1]):
                    if pos != b.start():
                        start = b.start()
                        end = start + len(word)
                ##
                print("|{:<30}| {:<8}| {:<5} |".format(word, start, end))
                
                data.append({
                    'string': word, 
                    'start': start, 
                    'end': end
                })
                
            pos += 1

        ##
        print(data)
        ##

        while repeat:
            for key, item in enumerate(data):
                while True:
                    print("#" * 50)
                    print("Address: ", address)
                    print("#")
                    print("String: ", item['string'])
                    print("#" * 50)
                    try:
                        label = input("Enter label OR (stop(s), skip(enter), repeat(r), next(n)): ")
                        if label == 'stop' or label == 's':
                            skip = False
                            stop = True
                            repeat = False
                        elif label == 'skip' or not label:
                            skip = True
                            repeat = False
                        elif label == 'repeat' or label == 'r':
                            repeat = True
                            break
                        elif label == 'next' or label == 'n':
                            next_address = True
                            repeat = False
                        else:
                            if re.match(r'^\d+$', label):
                                data[key]['label'] = labels[int(label)]
                                skip = False
                                stop = False
                                repeat = False
                                break
                            else:
                                raise IndexError
                    except IndexError:
                        print("#" * 50)
                        print("Error ID label. Please correct ID label enter")
                        continue
                
                    if skip or stop or next_address:
                        break
        
                if stop or repeat or next_address:
                    break
            
        ##

        print("#" * 50)
        print(data)

        if next_address is not True:
            if stop is not True:
                save_data(address, data)
                ready += 1
            else:
                print('Aborting pretrain!')
                sys.exit(0)
        else:
            ready += 1
            repeat = True
            print("#" * 50)
            print('Skip address')

        if ready > len(amount):
            sys.exit(0)
        else:
            repeat = True

##
# CREATE COLUMNS
#
def create_columns():
    temp = []

    for key, item in enumerate(labels): temp.append('')
        
    return dict(zip(labels, temp))
##
# SAVE DATA
#
def save_data(address, data):

    last_label = {}

    if exists(path_pretrain):
   
        ##
        columns = create_columns()
        ##
        with open(path_pretrain, 'a') as pretrain:
            writer = csv.writer(pretrain, delimiter=';')
            columns['Raw'] = address

            for key, item in enumerate(data):
                if 'label' in item:
                    label = [{'start': item['start'], 'end': item['end']}]
                    if len(last_label) and last_label['label'] == item['label']:
                        last_label['position'].append({'start': item['start'], 'end': item['end']})
                        columns[item['label']] = last_label['position']
                        label = last_label['position']
                    else:
                        columns[item['label']] = label
                    
                    last_label = {
                        'label': item['label'],
                        'position': label
                    }
               
            writer.writerow(columns.values())
            
    else:
        with open(path_pretrain, 'w') as pretrain:
            writer = csv.writer(pretrain, delimiter=';')
            columns = create_columns()
            writer.writerow(columns.keys())

            columns['Raw'] = address

            for key, item in enumerate(data):
                if 'label' in item:
                    label = [{'start': item['start'], 'end': item['end']}]
                    if len(last_label) and last_label['label'] == item['label']:
                        last_label['position'].append({'start': item['start'], 'end': item['end']})
                        columns[item['label']] = last_label['position']
                        label = last_label['position']
                    else:
                        columns[item['label']] = label
                    
                    last_label = {
                        'label': item['label'],
                        'position': label
                    }

            writer.writerow(columns.values())


if __name__ == "__main__":

    signal.signal(signal.SIGINT, interrupt)

    read_list()

    forever = threading.Event()
    forever.wait()

    