from translator_classes.classes import *

KEY = 'NzAwOTg4ZDgtMTkyZC00ODkwLWI4MjYtOGQ1NzUyMjkzMjgwOmNlOTI1NDliYWM1MjQxNjFhMDFkMjcwMWY5ZTQ0N2Jl'
translation = Translation(KEY)
token = translation.authentication().validate().get_token()

while True:
    word = input('Введите слово: ')
    translation.translate_from_rus_to_eng(word)
