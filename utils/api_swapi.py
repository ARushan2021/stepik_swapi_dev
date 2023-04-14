import allure

from utils.checking import Checking
from utils.http_methods import Http_methods

"""Методы для тестирования 'The Star Wars API'"""


class Get_swapi:
    api_hero = ''
    hero_name = ''

    """Получаем фильмы в которых играл наш герой"""


    @staticmethod
    def get_hero_films():
        with allure.step(f'Получаем фильмы в которых играл {Get_swapi.hero_name}'):
            url_hero = Get_swapi.api_hero
            result_hero = Http_methods.get(url_hero)
            Checking.check_all_status_code(result_hero, '200')
            Checking.print_check_all_status_code()
            Checking.check_json_token(result_hero, 'name')
            Checking.print_check_json_token()
            js_result_hero = result_hero.json()
            film_of_hero = js_result_hero["films"]
            return film_of_hero

    """Получаем ссылки на всех героев из фильмов с нашим героем и добавляем ссылки уникальных героев в список,
             самого нашего героя с список не вносим"""


    @staticmethod
    def get_people_with_hero_films(hero_films):
        with allure.step(f'Получаем ссылки на всех героев из фильмов с {Get_swapi.hero_name}'):
            characters_films_hero = []
            for i in range(0, len(hero_films)):
                url_films = hero_films[i]
                result_film = Http_methods.get(url_films)
                Checking.check_all_status_code(result_film, '200')
                Checking.check_json_token(result_film, 'title')
                js_result_film = result_film.json()
                characters_of_film = js_result_film['characters']
                for x in range(0, len(characters_of_film)):
                    if characters_of_film[x] not in characters_films_hero \
                            and characters_of_film[x] != Get_swapi.api_hero:
                        characters_films_hero.append(characters_of_film[x])
            Checking.print_check_all_status_code()
            Checking.print_check_json_token()
            return characters_films_hero

    """Добавляем имя каждого героя в файлик"""

    @staticmethod
    def writing_character_name_to_file(characters_films_hero):
        with allure.step('Добавляем имя каждого героя в файлик'):
            name_character_file = open(f"name_character/name_{Get_swapi.hero_name}.txt", "w")
            for i in range(0, len(characters_films_hero)):
                url_character = characters_films_hero[i]
                result_character = Http_methods.get(url_character)
                Checking.check_all_status_code(result_character, '200')
                Checking.check_json_token(result_character, 'name')
                # декодируем в windows-1251 по тому что, есть одно имя (people/35/ - "Padmé Amidala") с ударением,
                # utf-8 не может его распознать
                result_character.encoding = 'windows-1251'
                js_result_character = result_character.json()
                name_character = js_result_character['name']
                name_character_file.write(f'{i + 1}) {name_character} - "{url_character}" \n')
            name_character_file.close()
            Checking.print_check_all_status_code()
            Checking.print_check_json_token()
