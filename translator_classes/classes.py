import requests


# Класс для реализации отправки реквеста для аутентификации/получения токена
class TranslationResponse:
    def __init__(self, response):
        self.response = response

    # Данный метод валидирует наш запрос на аутентификацию
    # и возращает нам обратно класс TranslationResponse, если все прошло успешно
    def validate(self):
        if self.response.status_code == 200:
            print("Successfully authenticated! Getting token!")
            return TranslationResponse(self.response)
        else:
            raise Exception("Invalid response")

    # Метод, возвращающий нам токен
    def get_token(self):
        return self.response.text


#  Класс для реализации перевода с русского на англиский
class Translation:
    def __init__(self, key):
        self.auth_headers = {'Authorization':'Basic ' + key}
        self.authentication_url = 'https://developers.lingvolive.com/api/v1.1/authenticate'
        self.translation_url = 'https://developers.lingvolive.com/api/v1/Minicard'
        self.headers_translate = {'Authorization': 'Bearer {}'.format(self.authentication().get_token())}
        self.params = {'srcLang': 1049, 'dstLang': 1033}

    def authentication(self):
        return TranslationResponse(requests.post(self.authentication_url, headers=self.auth_headers))

    def translate_from_rus_to_eng(self, word):
        self.params['text'] = word

        request = requests.get(self.translation_url, headers=self.headers_translate, params=self.params)
        result = request.json()

        try:
            print(result['Translation']['Translation'])
        except:
            print("Provided word is not russian or something wrong happened!")