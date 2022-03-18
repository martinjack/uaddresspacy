![header](doc/header.png)
# Опис
[![PyPI version](https://badge.fury.io/py/uaddresspacy.svg)](https://badge.fury.io/py/uaddress)

Розбирання української адреси на типи

> Read this in other language: [English](README.en.md), [Русский](README.md), [Український](README.ua.md)

# Вимоги
* python3
* spacy
* re
* pandas
* csv
* os
* signal
* threading

## Підготовка моделі
```shell
python3 pretrain.py
```

## Створення моделі
```shell
python3 train.py
```

## Навчити модель
```shell
python3 -m spacy train config/config.cfg --paths.train training/train.spacy --paths.dev training/test.spacy --output models
```

## Навчити точніше модель
```shell
python3 -m spacy train config/config_acc.cfg --paths.train training/train.spacy --paths.dev training/test.spacy --output models
```

## Перевірка моделі
```shell
python3 example.py
```

### Створити файл опису моделі
```shell
python3 -m spacy init fill-config config/base_config.cfg config/config.cfg
```

### Створити файл опису більш точної моделі
```shell
python3 -m spacy init fill-config config/base_config_acc.cfg config/config_acc.cfg
```

## Приклади
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

## Структура
| Файл                      | Опис                                          |
| :-------------            | :-------------                                |
| pretrain.py               | Підготовка даних для навчання моделі          |
| train.py                  | Підготовка моделі                             |
| example.py                | Отримати приклад розбирання адреси на типи    |
| report.csv                | Приклад результату обробки на типи            |
| addresses.csv             | Список адрес для перевірки                    |
| training/raw.csv          | Дані для навчання                             |
| training/pretrain.csv     | Дані для навчання моделі                      |

## Типы
| Название                  | Опис                                          |
| :-------------            | :-------------                                |
| Country                   | Країна                                        |
| RegionType                | Тип області                                   |
| Region                    | Область                                       |
| CountyType                | Тип району                                    |
| County                    | Район                                         |
| Included                  | Входить до складу                             |
| LocalityType              | Тип населеного пункту                         |
| Locality                  | Населений пункт                               |
| StreetType                | Тип вулиці                                    |
| Street                    | Вулиця                                        |
| HousingType               | Тип корпусу                                   |
| Housing                   | Корпус                                        |
| HostelType                | Тип гуртожитку                                |
| Hostel                    | Гуртожиток                                    |
| HouseNumberType           | Тип номеру будинку                            |
| HouseNumber               | Номер будинку                                 |
| HouseNumberAdditionally   | Додатковий номер будинку                      |
| SectionType               | Тип секції                                    |
| Section                   | Секція                                        |
| ApartmentType             | Тип квартири                                  |
| Apartment                 | Квартира                                      |
| RoomType                  | Тип кімнати                                   |
| Room                      | Кімната                                       |
| Sector                    | Сектор                                        |
| FloorType                 | Тип поверху                                   |
| Floor                     | Поверх                                        |
| PostCode                  | Індекс                                        |
| Manually                  | Набір типів для подальшого розбирання адреси  |
| NotAddress                | Не адреса                                     |
| Comment                   | Коментар                                      |
| AdditionalData            | Додаткові дані                                |