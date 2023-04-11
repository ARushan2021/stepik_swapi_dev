"""Методы для проверки ответов на запросы"""


class Checking:
    lst_status_code = []
    expected_status_code = 200
    number_of_response = 0

    """Метод для проверки статус кода если был один запрос"""
    @staticmethod
    def check_status_code(response_result, expected_status_code):
        assert response_result.status_code == int(expected_status_code), \
            f'Получен не верный статус код {response_result.status_code}'
        print(f'Статус код верный - {response_result.status_code}')

    """Метод для проверки статус кода если было много запросов"""
    @staticmethod
    def check_all_status_code(response_result, expected_status_code):
        Checking.expected_status_code = expected_status_code
        assert response_result.status_code == int(Checking.expected_status_code), \
            f'Получен не верный статус код {response_result.status_code}'
        Checking.number_of_response += 1

    """Метод для вывода информационного сообщения о проверке статус кодов, если было много запросов"""
    @staticmethod
    def print_check_all_status_code():
        print(f'Колличество ответов на запросы - {Checking.number_of_response},'
              f' во всех статус код верный - {Checking.expected_status_code}')
        Checking.number_of_response = 0

