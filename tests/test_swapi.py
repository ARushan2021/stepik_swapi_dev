from utils.api_swapi import Get_swapi


"""Запись в файл имен людей, которые были во всех фильмах с Дартом Вейдером"""


class Test_swapi:

    def test_get_people_with_darth_vader(self):
        print('\n*** Метод "GET", возвращаем все фильмы где снимался Дарт Вейдер ***')
        results_dart = Get_swapi.get_darth_vader_films()
        print('*** Метод "GET", возвращаем всех героев из фильмов где снимался Дарт Вейдер ***')
        characters_films = Get_swapi.get_people_with_darth_vader_films(results_dart)
        print('*** Метод "GET", записываем в файлик всех героев из фильмов где снимался Дарт Вейдер ***')
        Get_swapi.writing_character_name_to_file(characters_films)




