#Python-translator
#API key: NzAwOTg4ZDgtMTkyZC00ODkwLWI4MjYtOGQ1NzUyMjkzMjgwOmNlOTI1NDliYWM1MjQxNjFhMDFkMjcwMWY5ZTQ0N2Jl
#token: ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmxlSEFpT2pFMk1Ua3lOemc1TWpFc0lrMXZaR1ZzSWpwN0lrTm9ZWEpoWTNSbGNuTlFaWEpFWVhraU9qVXdNREF3TENKVmMyVnlTV1FpT2pVd01Ea3NJbFZ1YVhGMVpVbGtJam9pTnpBd09UZzRaRGd0TVRreVpDMDBPRGt3TFdJNE1qWXRPR1ExTnpVeU1qa3pNamd3SW4xOS5SM2JmVnE1Y19QTXRGcDZ0V01PQ1VyN0VKZ1ZaWTFLV01ZajZ6bFVfOUFZ

import requests

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'NzAwOTg4ZDgtMTkyZC00ODkwLWI4MjYtOGQ1NzUyMjkzMjgwOmNlOTI1NDliYWM1MjQxNjFhMDFkMjcwMWY5ZTQ0N2Jl'

headers_auth = {'Authorization':'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)

if auth.status_code == 200:
    token = auth.text
    while True:
        word = input('Введите слово: ')
        if word:
            headers_translate = {
                'Authorization': 'Bearer ' + token
            }
            params = {
                'text': word,
                'srcLang': 1049,
                'dstLang': 1033
            }
            request = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
            res = request.json()
            try:
                print(res['Translation']['Translation'])
            except:
                print('Это русско-английский словарь!')

else:
    print('Error!')