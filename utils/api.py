from utils.http_methods import Http_methods

"""Методы для тестирования 'The Star Wars API'"""


class Get_swapi:

    link_of_darth_vader = 'https://swapi.dev/api/people/4/'

    @staticmethod
    def get_darth_vader_films():
        """Узнаем фильмы в которых играл Дарт Вейдер"""
        url_darth_vader = Get_swapi.link_of_darth_vader
        result_darth_vader = Http_methods.get(url_darth_vader)
        js_result_darth_vader = result_darth_vader.json()
        film_of_darth_vader = js_result_darth_vader["films"]
        return film_of_darth_vader

    @staticmethod
    def get_people_with_darth_vader_films(darth_vader_films):
        """Получаем ссылки на всех героев из фильмов с Дартом Вейдером и добавляем ссылки уникальных героев в список,
         самого Дарта Вейдера с список не вносим"""
        characters_films_darth_vader = []
        for i in range(0, len(darth_vader_films)):
            url_films = darth_vader_films[i]
            result_film = Http_methods.get(url_films)
            js_result_film = result_film.json()
            characters_of_film = js_result_film['characters']
            for x in range(0, len(characters_of_film)):
                if characters_of_film[x] not in characters_films_darth_vader\
                        and characters_of_film[x] != Get_swapi.link_of_darth_vader:
                    characters_films_darth_vader.append(characters_of_film[x])
        return characters_films_darth_vader

    @staticmethod
    def writing_character_name_to_file(characters_films_darth_vader):
        """Добавляем имя каждого героя в файлик"""
        name_character_file = open("name_character/name_character.txt", "w")
        for i in range(0, len(characters_films_darth_vader)):
            url_character = characters_films_darth_vader[i]
            result_character = Http_methods.get(url_character)
            #декодируем в windows-1251, по тому что есть одно имя (people/35/ - "Padmé Amidala") с ударением,
            # utf-8 не может его распознать
            result_character.encoding = 'windows-1251'
            js_result_character = result_character.json()
            name_character = js_result_character['name']
            name_character_file.write(f'{i+1}) {name_character} - "{url_character}" \n')
        name_character_file.close()







ts = Get_swapi()
tse = ts.get_darth_vader_films()
ts.get_people_with_darth_vader_films(tse)

