import json

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:151.0) Gecko/20100101 Firefox/151.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://www.nzpost.co.nz/tools/tracking',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'pragma': 'no-cache',
    'Origin': 'https://www.nzpost.co.nz',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Priority': 'u=4',
}
def lookup(tracking_reference):
    params = {
        'tracking_reference': tracking_reference,
    }

    response = requests.get('https://tools.nzpost.co.nz/tracking/api/parceltrack/parcels', params=params, headers=headers)

    if response.status_code != 200:
        return False
    else:
        return response.json()