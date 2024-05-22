import requests

cookies = {
    '_gcl_au': '1.1.1442243864.1713255933',
    '_ga': 'GA1.1.1058116410.1713255936',
    '_lr_env_src_ats': 'false',
    '_cc_id': '56fdfd46609c190652e38f6a44472332',
    'pbjs-unifiedid_cst': 'Ryz5LF8s6Q%3D%3D',
    '_ga_HNQ9P9MGZR': 'deleted',
    '_ga_HNQ9P9MGZR': 'deleted',
    'pbjs-unifiedid': '%7B%22TDID%22%3A%2288d825cd-1154-4c8a-8d47-7a96e5fb7dcd%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222024-04-05T09%3A22%3A03%22%7D',
    '__qca': 'P0-965765815-1715082045523',
    'clever-last-tracker-66554': '2',
    '__gads': 'ID=fe15d861da8b5b45:T=1713255936:RT=1716209236:S=ALNI_MbWziKEO6jg3AzTrqH-yyTbQIP4GQ',
    '__gpi': 'UID=00000d5e7e9c9538:T=1713255936:RT=1716209236:S=ALNI_MbP87U_ZjGgdrSGniPcqjrxFIuVUw',
    '__eoi': 'ID=567119f5bba094c0:T=1713255936:RT=1716209236:S=AA-Afjbp8Hd5iH-ahPGnKO5ocbH3',
    'FCNEC': '%5B%5B%22AKsRol85VJGAXFgKUoIqCKOpRghgme9p8va-8GMIQ0asZbE_xncXaKDN42N5jBwYbv-QUtOGxUP8WBufldCy4vS_88v8YOIOYeMz-BLcS19_urcnOxuv_bU2WjGoLyBZ1R8BUnMtGZpgOWj-f126zAwkd_rLDu_fqQ%3D%3D%22%5D%5D',
    '_ga_QH2YGS7BB4': 'GS1.1.1716209162.150.1.1716209529.0.0.0',
    '_ga_3KF4XTPHC4': 'GS1.1.1716209162.149.1.1716209529.60.0.0',
    '_ga_HNQ9P9MGZR': 'GS1.1.1716209165.94.1.1716209529.60.0.0',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-ZA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '_gcl_au=1.1.1442243864.1713255933; _ga=GA1.1.1058116410.1713255936; _lr_env_src_ats=false; _cc_id=56fdfd46609c190652e38f6a44472332; pbjs-unifiedid_cst=Ryz5LF8s6Q%3D%3D; _ga_HNQ9P9MGZR=deleted; _ga_HNQ9P9MGZR=deleted; pbjs-unifiedid=%7B%22TDID%22%3A%2288d825cd-1154-4c8a-8d47-7a96e5fb7dcd%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222024-04-05T09%3A22%3A03%22%7D; __qca=P0-965765815-1715082045523; clever-last-tracker-66554=2; __gads=ID=fe15d861da8b5b45:T=1713255936:RT=1716209236:S=ALNI_MbWziKEO6jg3AzTrqH-yyTbQIP4GQ; __gpi=UID=00000d5e7e9c9538:T=1713255936:RT=1716209236:S=ALNI_MbP87U_ZjGgdrSGniPcqjrxFIuVUw; __eoi=ID=567119f5bba094c0:T=1713255936:RT=1716209236:S=AA-Afjbp8Hd5iH-ahPGnKO5ocbH3; FCNEC=%5B%5B%22AKsRol85VJGAXFgKUoIqCKOpRghgme9p8va-8GMIQ0asZbE_xncXaKDN42N5jBwYbv-QUtOGxUP8WBufldCy4vS_88v8YOIOYeMz-BLcS19_urcnOxuv_bU2WjGoLyBZ1R8BUnMtGZpgOWj-f126zAwkd_rLDu_fqQ%3D%3D%22%5D%5D; _ga_QH2YGS7BB4=GS1.1.1716209162.150.1.1716209529.0.0.0; _ga_3KF4XTPHC4=GS1.1.1716209162.149.1.1716209529.60.0.0; _ga_HNQ9P9MGZR=GS1.1.1716209165.94.1.1716209529.60.0.0',
    'referer': 'https://www.sofascore.com/tennis',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36',
    'x-requested-with': '89df4e',
}
def split_odds(x):
    lst = x.split('/')
    lst = int(lst[0])/int(lst[1])
    return round(lst,3)

def get_odds(x):
    


    try:
        response = requests.get(
        f'https://www.sofascore.com/api/v1/event/{x}/provider/1/winning-odds',
        cookies=cookies,
        headers=headers,
    ).json()
        away_odds = response['away']['fractionalValue']
        home_odds = response['home']['fractionalValue']
        home_odds = split_odds(home_odds)
        away_odds = split_odds(away_odds)
        return [home_odds,away_odds]
    except:
        return []

#print(get_odds(12342401))