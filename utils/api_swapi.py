from utils.http_methods import Http_methods
from utils.checking import Checking

"""Методы для тестирования 'The Star Wars API'"""


class Get_swapi:
    api_darth_vader = 'https://swapi.dev/api/people/4/'

    """Получаем фильмы в которых играл Дарт Вейдер"""
    @staticmethod
    def get_darth_vader_films():
        url_darth_vader = Get_swapi.api_darth_vader
        result_darth_vader = Http_methods.get(url_darth_vader)
        Checking.check_status_code(result_darth_vader, '200')
        js_result_darth_vader = result_darth_vader.json()
        film_of_darth_vader = js_result_darth_vader["films"]
        return film_of_darth_vader

    """Получаем ссылки на всех героев из фильмов с Дартом Вейдером и добавляем ссылки уникальных героев в список,
             самого Дарта Вейдера с список не вносим"""
    @staticmethod
    def get_people_with_darth_vader_films(darth_vader_films):
        characters_films_darth_vader = []
        for i in range(0, len(darth_vader_films)):
            url_films = darth_vader_films[i]
            result_film = Http_methods.get(url_films)
            Checking.check_all_status_code(result_film, '200')
            js_result_film = result_film.json()
            characters_of_film = js_result_film['characters']
            for x in range(0, len(characters_of_film)):
                if characters_of_film[x] not in characters_films_darth_vader \
                        and characters_of_film[x] != Get_swapi.api_darth_vader:
                    characters_films_darth_vader.append(characters_of_film[x])
        Checking.print_check_all_status_code()
        return characters_films_darth_vader

    """Добавляем имя каждого героя в файлик"""
    @staticmethod
    def writing_character_name_to_file(characters_films_darth_vader):
        name_character_file = open("name_character/name_character.txt", "w")
        for i in range(0, len(characters_films_darth_vader)):
            url_character = characters_films_darth_vader[i]
            result_character = Http_methods.get(url_character)
            Checking.check_all_status_code(result_character, '200')
            # декодируем в windows-1251 по тому что, есть одно имя (people/35/ - "Padmé Amidala") с ударением,
            # utf-8 не может его распознать
            result_character.encoding = 'windows-1251'
            js_result_character = result_character.json()
            name_character = js_result_character['name']
            name_character_file.write(f'{i + 1}) {name_character} - "{url_character}" \n')
        name_character_file.close()
        Checking.print_check_all_status_code()
