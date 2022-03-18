![header](doc/header.png)
# Описание
[![PyPI version](https://badge.fury.io/py/uaddresspacy.svg)](https://badge.fury.io/py/uaddresspacy)

Parsing Ukrainian addresses into types

> Read this in other language: [English](README.en.md), [Русский](README.md), [Український](README.ua.md)

# Requirements
* python3
* spacy
* re
* pandas
* csv
* os
* signal
* threading

## Model preparation
```shell
python3 pretrain.py
```

## Model creation
```shell
python3 train.py
```

## Train model
```shell
python3 -m spacy train config/config.cfg --paths.train training/train.spacy --paths.dev training/test.spacy --output models
```

## Train model more accurately
```shell
python3 -m spacy train config/config_acc.cfg --paths.train training/train.spacy --paths.dev training/test.spacy --output models
```

## Model check
```shell
python3 example.py
```

### Create model description file
```shell
python3 -m spacy init fill-config config/base_config.cfg config/config.cfg
```

### Create description file for a more accurate model
```shell
python3 -m spacy init fill-config config/base_config_acc.cfg config/config_acc.cfg
```

## Examples
```python
import uaddresspacy

print(uaddresspacy.parse(", - полтавська чутівський жовтневе вул. -, буд. -, кв.,"))
# [('полтавська', 'Locality'), ('чутівський', 'CountyType'), ('жовтневе', 'Locality'), ('вул.', 'StreetType'), ('буд.', 'HouseNumberType'), ('кв.', 'ApartmentType')]
print(uaddresspacy.parse(", 01000 київ, місто київ, місто київ воровського, буд. 43-б, кв. 14,"))
# [('01000', 'PostCode'), ('київ', 'Region'), ('місто', 'LocalityType'), ('київ', 'Locality'), ('воровського', 'Street'), ('буд.', 'HouseNumberType'), ('43-б', 'HouseNumber'), ('кв.', 'ApartmentType'), ('14', 'Apartment')]
```
![use](doc/use.gif)

```sh
python3 pretrain.py
```
![pretrain](doc/pretrain.gif)

## Structure
| File                      | Description                                   |
| :-------------            | :-------------                                |
| pretrain.py               | Preparing data for model training             |
| train.py                  | Model preparation                             |
| example.py                | Get example parsings address on types         |
| report.csv                | Example parsing address on types              |
| addresses.csv             | List of addresses to check                    |
| training/raw.csv          | Data for training                             |
| training/pretrain.csv     | Data to train model                           |

## Типы
| Name                      | Description                                   |
| :-------------            | :-------------                                |
| Country                   | Country                                       |
| RegionType                | Type region                                   |
| Region                    | Region                                        |
| CountyType                | Type county                                   |
| County                    | County                                        |
| Included                  | Included                                      |
| LocalityType              | Type locality                                 |
| Locality                  | Locality                                      |
| StreetType                | Type street                                   |
| Street                    | Street                                        |
| HousingType               | Type housing                                  |
| Housing                   | Housing                                       |
| HostelType                | Type hostel                                   |
| Hostel                    | Hostel                                        |
| HouseNumberType           | Type housenumber                              |
| HouseNumber               | HouseNumber                                   |
| HouseNumberAdditionally   | Additionally housenumber                      |
| SectionType               | Type section                                  |
| Section                   | Section                                       |
| ApartmentType             | Type apartment                                |
| Apartment                 | Apartment                                     |
| RoomType                  | Type room                                     |
| Room                      | Room                                          |
| Sector                    | Sector                                        |
| FloorType                 | Type floor                                    |
| Floor                     | Floor                                         |
| PostCode                  | Postcode                                      |
| Manually                  | Manually                                      |
| NotAddress                | Not address                                   |
| Comment                   | Comment                                       |
| AdditionalData            | Additional data                               |