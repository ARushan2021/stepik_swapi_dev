import json
import requests

"""Методы для проверки ответов на запросы"""


class Checking:
    expected_status_code = 200
    number_of_response = 0

    """Метод для проверки статус кода и подсчитывания кол.во запросов"""
    @staticmethod
    def check_all_status_code(response_result, expected_status_code):
        Checking.expected_status_code = expected_status_code
        assert response_result.status_code == int(Checking.expected_status_code), \
            f'Получен не верный статус код {response_result.status_code}'
        Checking.number_of_response += 1

    """Метод для вывода информационного сообщения о проверке статус кодов"""
    @staticmethod
    def print_check_all_status_code():
        print(f'Колличество ответов на запросы - {Checking.number_of_response},'
              f' во всех статус код верный - {Checking.expected_status_code}')
        Checking.number_of_response = 0

    """Метод для проверки наличия обязательных полей"""
    @staticmethod
    def check_json_token(response_result, expected_value):
        token = json.loads(response_result.text)
        assert list(token) == expected_value, 'Ошибка!!! Не хватет обязательных полей в ответе!!!'

    @staticmethod
    def print_check_json_token():
        print('Во всех запросах присутствуют обязательные поля')









    @staticmethod
    def json_token(response_result):
        token = json.loads(response_result.text)
        print(list(token))
