class Vacancy:
    """
    Класс работы с вакансиями и сравнение зарплат
    """

    __slots__ = ("__name", "__link", "__salary", "__description", "__area")

    def __init__(self, vac):
        self.__name = vac["name"] if vac["name"] else "Название не указано"
        self.__link = (
            vac["alternate_url"] if vac["alternate_url"] else "Ссылка не указана"
        )
        self.__salary = (
            vac["salary"]["from"] if vac["salary"] and vac["salary"]["from"] else 0
        )
        self.__description = (
            vac["snippet"]["responsibility"]
            if vac["snippet"] and vac["snippet"]["responsibility"]
            else "Описание отсутствует"
        )
        self.__area = (
            vac["area"]["name"]
            if vac["area"] and vac["area"]["name"]
            else "Город не указан"
        )

    @property
    def name(self):
        return self.__name

    @property
    def link(self):
        return self.__link

    @property
    def salary(self):
        return self.__salary

    @property
    def description(self):
        return self.__description

    @property
    def area(self):
        return self.__area

    def __str__(self):
        name = f"Вакансия: {self.name}"
        link = f"Ссылка: {self.link}"
        sal = f"Зарплата: {self.salary}"
        desc = f"Описание: {self.description}"
        area = f"Место: {self.area}"
        return f" {name}, {link}, {sal}, {desc}, {area}"

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary


if __name__ == "__main__":
    vacancy2 = {
        "name": "Разработчик",
        "alternate_url": None,
        "salary": None,
        "snippet": None,
        "area": None,
    }
    a = Vacancy(vacancy2)
    print(a)
