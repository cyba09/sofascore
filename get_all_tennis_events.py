import requests
import get_winning_odds
import get_player_rankings
import const

CUTOFF_ODD = 0.45
CUTOFF_RANKING = 75
dte = const.DTE

def get_lowest_odd(x):
    if x[0] < x[1]:
        y = x[0]
    else:
        y = x[1]
    if y < CUTOFF_ODD:
        return True
    else:
        return False

def get_ranking_difference(x):
    y = abs(x[0]-x[1])
    if y > CUTOFF_RANKING:
        return True
    else:
        return False

def compare_odds_rankings(x,y):
    if ((x[0] - x[1]) * (y[0] - y[1])) > 0:
        return True
    else:
        return False


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
    'clever-last-tracker-66554': '1',
    'FCNEC': '%5B%5B%22AKsRol9rH77FlV19SmYzT8fd5ys8pWUuxBvFSPQiVXBfJUxdiH4c9ziTekytr7o0BxNZsXg4zMVYnfBSeLFI2p87AVW7Dx53sxSd9XFYePoBUEFIw6gChOY-nfkPl0e6nC70KMbWgmIcE69zxR3QT1FapHyBgPGWtg%3D%3D%22%5D%5D',
    '__gads': 'ID=fe15d861da8b5b45:T=1713255936:RT=1716193324:S=ALNI_MbWziKEO6jg3AzTrqH-yyTbQIP4GQ',
    '__gpi': 'UID=00000d5e7e9c9538:T=1713255936:RT=1716193324:S=ALNI_MbP87U_ZjGgdrSGniPcqjrxFIuVUw',
    '__eoi': 'ID=567119f5bba094c0:T=1713255936:RT=1716193324:S=AA-Afjbp8Hd5iH-ahPGnKO5ocbH3',
    '_ga_QH2YGS7BB4': 'GS1.1.1716186458.145.1.1716193451.0.0.0',
    '_ga_3KF4XTPHC4': 'GS1.1.1716186458.144.1.1716193451.60.0.0',
    '_ga_HNQ9P9MGZR': 'GS1.1.1716186463.89.1.1716193451.54.0.0',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-ZA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '_gcl_au=1.1.1442243864.1713255933; _ga=GA1.1.1058116410.1713255936; _lr_env_src_ats=false; _cc_id=56fdfd46609c190652e38f6a44472332; pbjs-unifiedid_cst=Ryz5LF8s6Q%3D%3D; _ga_HNQ9P9MGZR=deleted; _ga_HNQ9P9MGZR=deleted; pbjs-unifiedid=%7B%22TDID%22%3A%2288d825cd-1154-4c8a-8d47-7a96e5fb7dcd%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222024-04-05T09%3A22%3A03%22%7D; __qca=P0-965765815-1715082045523; clever-last-tracker-66554=1; FCNEC=%5B%5B%22AKsRol9rH77FlV19SmYzT8fd5ys8pWUuxBvFSPQiVXBfJUxdiH4c9ziTekytr7o0BxNZsXg4zMVYnfBSeLFI2p87AVW7Dx53sxSd9XFYePoBUEFIw6gChOY-nfkPl0e6nC70KMbWgmIcE69zxR3QT1FapHyBgPGWtg%3D%3D%22%5D%5D; __gads=ID=fe15d861da8b5b45:T=1713255936:RT=1716193324:S=ALNI_MbWziKEO6jg3AzTrqH-yyTbQIP4GQ; __gpi=UID=00000d5e7e9c9538:T=1713255936:RT=1716193324:S=ALNI_MbP87U_ZjGgdrSGniPcqjrxFIuVUw; __eoi=ID=567119f5bba094c0:T=1713255936:RT=1716193324:S=AA-Afjbp8Hd5iH-ahPGnKO5ocbH3; _ga_QH2YGS7BB4=GS1.1.1716186458.145.1.1716193451.0.0.0; _ga_3KF4XTPHC4=GS1.1.1716186458.144.1.1716193451.60.0.0; _ga_HNQ9P9MGZR=GS1.1.1716186463.89.1.1716193451.54.0.0',
    'if-none-match': 'W/"97bd3a961b"',
    'referer': 'https://www.sofascore.com/tennis',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36',
    'x-requested-with': '2e9fda',
}

response = requests.get(
    f'https://www.sofascore.com/api/v1/sport/tennis/scheduled-events/{dte}',
    cookies=cookies,
    headers=headers,
).json()
all_data =[]

for game in response['events']:
    
    game_id = game['id']
    home_slug = game['homeTeam']['slug']
    home_id = game['homeTeam']['id']
    away_slug = game['awayTeam']['slug']
    away_id = game['awayTeam']['id']
    tournament = game['tournament']['name']
    
    all_data.append([game_id,home_slug,home_id,away_slug,away_id,tournament])

for game in all_data:
    #print(f'trying {game[1]}')
    #####################################odds
    odds = get_winning_odds.get_odds(game[0])
    if not odds:
        continue
    if not get_lowest_odd(odds):
        continue
    ##########################################ranking
    rankings = get_player_rankings.get_rankings(game[0])
    if not rankings:
        continue
    if not get_ranking_difference(rankings):
        continue
    ####################odds/ranking comparison
    if not compare_odds_rankings(odds,rankings):
        continue
    ######################
    print(game[1],game[-1])
print('done')

    