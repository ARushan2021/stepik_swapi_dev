import allure

from utils.api_swapi import Get_swapi

"""Запись в файл имен персонажей, которые были во всех фильмах с выбранным героем"""


@allure.epic('Тестирование портала "The Star Wars API"')
class Test_swapi:

    @allure.title('Получаем список всех героев которые снимались в месте с Darth_Wader')
    def test_get_people_with_darth_vader(self):
        Get_swapi.api_hero = 'https://swapi.dev/api/people/4/'
        Get_swapi.hero_name = 'Darth_Wader'
        print(f'\n*** Метод "GET", возвращаем все фильмы где снимался {Get_swapi.hero_name} ***')
        results_hero = Get_swapi.get_hero_films()
        print(f'*** Метод "GET", возвращаем всех героев из фильмов где снимался {Get_swapi.hero_name} ***')
        characters_films = Get_swapi.get_people_with_hero_films(results_hero)
        print(f'*** Метод "GET", записываем в файлик всех героев из фильмов где снимался {Get_swapi.hero_name}р ***')
        Get_swapi.writing_character_name_to_file(characters_films)

    @allure.title('Получаем список всех героев которые снимались в месте с Owen_Lars')
    def test_get_people_with_luke_skywalker(self):
        Get_swapi.api_hero = 'https://swapi.dev/api/people/6/'
        Get_swapi.hero_name = 'Owen_Lars'
        print(f'\n*** Метод "GET", возвращаем все фильмы где снимался {Get_swapi.hero_name} ***')
        results_hero = Get_swapi.get_hero_films()
        print(f'*** Метод "GET", возвращаем всех героев из фильмов где снимался {Get_swapi.hero_name} ***')
        characters_films = Get_swapi.get_people_with_hero_films(results_hero)
        print(f'*** Метод "GET", записываем в файлик всех героев из фильмов где снимался {Get_swapi.hero_name} ***')
        Get_swapi.writing_character_name_to_file(characters_films)

# allure serve test_reports - формирование allure в html
