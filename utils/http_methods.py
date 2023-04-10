import requests

"""Список Http методов для тестирования 'The Star Wars API'"""


class Http_methods:
    headers = {'Content-Type': 'application/json'}

    @staticmethod
    def get(url):
        result = requests.get(url, headers=Http_methods.headers)
        return result

