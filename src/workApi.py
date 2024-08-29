from abc import ABC, abstractmethod
from typing import List

import requests


class Parser(ABC):
    """
    Абстрактный родительский класс для подключения по API
    """

    @abstractmethod
    def load_vacancies(self, keyword):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом
    """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []
        # self.validate_vacancies = []

    def load_vacancies(self, keyword: str):
        """
        Функция для получения вакансий по заданному слову.
        Приводит полученный список к нужному виду.
        """
        self.params["text"] = keyword
        while self.params.get("page") != 2:
            try:
                response = requests.get(
                    self.__url, headers=self.__headers, params=self.params
                )
            except Exception as e:
                print(f"Произошла ошибка {e}")
            else:
                vacancies = response.json()["items"]
                self.vacancies.extend(vacancies)
                self.params["page"] += 1

    def get_vacancies(self) -> List:
        """
        Возвращает список вакансий
        """
        return self.vacancies


if __name__ == "__main__":
    hh = HeadHunterAPI()
    hh.load_vacancies("Python")
    hh_vacancies = hh.get_vacancies()
    print(hh_vacancies)
