import json

import requests
from tqdm import tqdm


def load_data_from_api():
    request = requests.get('http://hubeau.eaufrance.fr/api/v1/hydrometrie/observations_tr')
    data = request.json()['data']
    print(data)
    return data


# def load_all_data_from_api():
#     i = 0
#     request = requests.get('http://hubeau.eaufrance.fr/api/v1/hydrometrie/observations_tr')
#     data = request.json()['data']
#     print(data)
#     next_page = request.json()['next']
#     print(next_page)
#     while next_page is not None:
#         request = requests.get(next_page)
#         for info in tqdm(request):
#             print(info)
#         i += 1
#         print(f'{i} data loaded')
#

# def load_all_code_site_from_api():
#     i = 0
#     request = requests.get('http://hubeau.eaufrance.fr/api/v1/hydrometrie/observations_tr')
#     data = request.json()['data'][0]['code_site']
#     print(data)
#     next_page = request.json()['next']
#     print(next_page)
#     while next_page is not None:
#         next_page = request.json()['next']
#         request = requests.get(next_page)
#         print(next_page)
#         data = request.json()['data'][0]['code_site']
#         print(data)
#         i += 1
#         print(f'{i} data loaded')


def load_all_grandeur_hydro_from_api():
    i = 0
    request = requests.get('http://hubeau.eaufrance.fr/api/v1/hydrometrie/observations_tr')
    data = request.json()['data'][0]['grandeur_hydro']
    print(data)
    next_page = request.json()['next']
    print(next_page)
    while next_page is not None:
        next_page = request.json()['next']
        request = requests.get(next_page)
        data = request.json()['data'][0]['grandeur_hydro']
        print(data)
        i += 1
        print(f'{i} data loaded')


# load_all_data_from_api()
# load_all_code_site_from_api()


def load_all_code_site_from_api():
    i = 0
    mylist = []
    request = requests.get('http://hubeau.eaufrance.fr/api/v1/hydrometrie/observations_tr')
    list = request.json()['data']
    next_page = request.json()['next']
    for element in list:
        mylist.append(element['code_site'])
    print(mylist)
    print(next_page)
    while next_page is not None:
            next_page = request.json()['next']
            request = requests.get(next_page)
            list = request.json()['data']
            for element in list:
                mylist.append(element['code_site'])
            print(mylist)
            i += 1
            print(f'{i} data loaded')


load_all_code_site_from_api()
