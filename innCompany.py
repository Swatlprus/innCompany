# https://github.com/hflabs/dadata-py

from dadata import Dadata

token = "" # Токен с сервиса DaData
secret = "" # Секретный ключ с сервиса DaData


def check(name,query):
    dadata = Dadata(token, secret) # Данные для авторизации в сервисе DaData
    infoCompany = dadata.find_by_id(name, query) # Поиск информации о компании
    if infoCompany[0]['data']['type'] == 'LEGAL':
        print(infoCompany[0]['data']['name']['full']) # Названия компании
        print(infoCompany[0]['data']['type']) # Тип компании
        print(infoCompany[0]['data']['opf']['full']) # Полный префикс компании
        print(infoCompany[0]['data']['opf']['short'])  # Короткий префикс компании
        print(infoCompany[0]['data']['address']['data']['region_type_full']) # Тип региона
        print(infoCompany[0]['data']['address']['data']['region']) # Название региона
        print(infoCompany[0]['data']['address']['data']['city_type'])  # Название города
        print(infoCompany[0]['data']['address']['data']['city']) # Название города
        print(infoCompany[0]['data']['address']['data']['street_type_full']) # Тип улица/проспект
        print(infoCompany[0]['data']['address']['data']['street']) # Название улицы
        print(infoCompany[0]['data']['address']['data']['house_type_full']) # Тип улица/проспект
        print(infoCompany[0]['data']['address']['data']['house']) # Название улицы
    else:
        print(infoCompany[0]['data']['name']['full'])  # Названия компании
        print(infoCompany[0]['data']['type'])  # Тип компании
        print(infoCompany[0]['data']['opf']['full'])  # Полный префикс компании
        print(infoCompany[0]['data']['opf']['short'])  # Короткий префикс компании
        print(infoCompany[0]['data']['address']['data']['region_type_full'])  # Тип региона
        print(infoCompany[0]['data']['address']['data']['region'])  # Название региона

check(name='party', query='0274940895') # Проверка компании по ИНН 0274940895