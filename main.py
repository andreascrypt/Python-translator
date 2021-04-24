from translator_classes.classes import *

KEY = 'NzAwOTg4ZDgtMTkyZC00ODkwLWI4MjYtOGQ1NzUyMjkzMjgwOmNlOTI1NDliYWM1MjQxNjFhMDFkMjcwMWY5ZTQ0N2Jl'
translation = Translation(KEY)
token = translation.authentication().validate().get_token()

while True:
    word = input('Введите слово: ')
    translation.translate_from_rus_to_eng(word)


# TODO:
# 1) Реализовать работу приложения таким образом, чтобы у тебя была фактические одна строчка в main.py для его запуска
# Translation(KEY).start() # строчка с ключем пока не считается :)
# Собственно, тебе потребуется добавить в класс Translation новый метод start()
# И добработать метод translate_from_rus_to_eng()

# ***2) Доводим до такого формата: Translation().start()
# - Прочитать про environment variables
# - Добавить переменную среды к себе на машину
# - Найти способ забрать значение этой переменной
# - Реализовать метод в классе Translation, который будет забирать значение твоей переменной
# и подставлять значение key тут: self.auth_headers = {'Authorization':'Basic ' + key}