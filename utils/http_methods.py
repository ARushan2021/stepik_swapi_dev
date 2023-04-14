import requests

from utils.logger import Logger

"""Список Http методов для тестирования 'The Star Wars API'"""


class Http_methods:
    headers = {'Content-Type': 'application/json'}
    cookies = ""

    @staticmethod
    def get(url):
        Logger.add_request(url, method="GET")
        result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookies)
        Logger.add_response(result)
        return result

