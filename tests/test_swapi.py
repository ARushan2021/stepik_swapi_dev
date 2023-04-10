from utils.api import Get_swapi

"""Запись в файл имен людей, которые были во всех фильмах с Дартом Вейдером"""


class Test_swapi:

    def test_get_people_with_darth_vader(self):
        results_dart = Get_swapi.get_darth_vader_films()
        characters_films = Get_swapi.get_people_with_darth_vader_films(results_dart)
        Get_swapi.writing_character_name_to_file(characters_films)




