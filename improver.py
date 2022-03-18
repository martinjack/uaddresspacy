import re

##
# IMPROVE ADDRESS
#
def improve_address(address):
    address = re.sub(r'(\,)(?!\s)', ', ', address)
    address = re.sub(r'(?<=[a-zA-Zа-яА-ЯіІїЇґҐєЄ])\-\s|\s\-(?=[a-zA-Zа-яА-ЯіІїЇґҐєЄ])', '-', address)
    address = re.sub(r'^\,\s|\,$|^\s+', '', address)
    address = re.sub(r'\,', '', address)
    address = re.sub(r'\s\.', '.', address)
    address = re.sub(r'\(', ' (', address)
    address = re.sub(r'\)', ') ', address)
    address = re.sub(r'\s+', ' ', address)
    address = re.sub(r'\s$', '', address)
    address = re.sub(r'\.(?!(\s|\,|$|\)))', '. ', address)
    address = re.sub(r'(?<=[a-zA-Zа-яА-ЯіІїЇґҐєЄ])(?=\d+)', ' ', address)
    address = re.sub(r'[\’\`\”\'“\"_]+(?=[a-zA-Zа-яА-ЯіІїЇґҐєЄ][”])|(?<=[”][a-zA-Zа-яА-ЯіІїЇґҐєЄ])[\’\`\”\'“\"_]+', '', address)
    address = re.sub(r'(?<=\d)(?=[a-zA-Zа-яА-ЯіІїЇґҐєЄ])', ' ', address)
    address = re.sub(r'\\', '/', address)
    address = re.sub(r'\-{2,}|\s\-(\s|$)', ' ', address)
    address = re.sub(r'(?<=[a-zA-Zа-яА-ЯіІїЇґҐєЄ])(?=\№)', ' ', address)
    address = re.sub(r'(?<=\№)(?=\d+)', ' ', address)
    
    address = improve_quotes(address)

    return address
##
# IMPROVE QUOTES
#
def improve_quotes(str):
    str = re.sub(r'[\’\`\”\'“\"_]', '’', str)
    str = re.sub(r'\’{2,}', '', str)

    return str
##
# STR TO REGEX
#
def str_to_regex(str):
    
    str = re.sub(r'\(', '\(', str)
    str = re.sub(r'\)', '\)', str)
    str = re.sub(r'\.', '\.', str)

    return str