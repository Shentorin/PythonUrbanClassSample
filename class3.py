class Russian_movie:

    def __init__(self, name: str, release_date: int, budget: int, list_of_actors: list):
        """
         Создание и подготовка к работе объекта "Русский фильм"

        :param name: Название фильма
        :param release_date: Дата выхода
        :param budget: Бюджет фильма
        :param list_of_actors: Список актеров, участвующих в фильме
        """
        self.name = name
        self.release_date = release_date
        self.budget = budget
        self.list_of_actors = list_of_actors
        

    def request_money_from_the_Ministry_of_Culture (self, budget: None) -> int:
        """
         Запросить деньги на фильм у Минкульта, вне зависимости от изначального бюджета

        :return: Бюджет фильма после запроса
        """

    def check_Petrov (self, list_of_actors: list) -> bool:
        """
         Проверить, есть ли в фильме Петров

        :return: True - если Петров в списке актеров
                 или
                 False - если Петрова нет в списке
        """
    def show_movie_description (self) -> str:
        """
        Показать описание фильма
        :return: Описание фильма
        """

if __name__ == "__main__":
    russian_movie = Russian_movie("Учение", 2016, 1000000, [
                    "Виктория Исакова",
                    "Пётр Скворцов",  
                    "Александр Горчилин",
                    ...
                                                           ] 
                                 ) 
