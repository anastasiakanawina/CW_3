class Vacancy:
    all_vacancies = []

    def __init__(self, vac_id, title, link, salary, description):

        self.vac_id = vac_id
        self.title = title
        self.link = link
        self.salary = salary if salary is not None else 0
        self.description = description

    def __str__(self):
        return f"ID: {self.vac_id}\nTitle: {self.title}\nLink: {self.link}\nSalary: {self.salary}\nDescription: {self.description}"

    def __lt__(self, other):
        # Метод сравнения вакансий по зарплате
        if self.salary and other.salary:
            return self.salary < other.salary
        return False

    @classmethod
    def vacancies_from_hh(cls, list):

        for vacancy in list:
            cls.all_vacancies.append(Vacancy
                                     (vac_id=vacancy['id'],
                                      title=vacancy['name'],
                                      link=vacancy['alternate_url'],
                                      salary=vacancy.get('payment_from'),
                                      description=vacancy['snippet']['requirement']))

    @classmethod
    def vacancies_from_sj(cls, list):

        for vacancy in list:
            cls.all_vacancies.append(Vacancy
                                     (vac_id=vacancy['id'],
                                      title=vacancy['profession'],
                                      link=vacancy['link'],
                                      salary=vacancy['payment_from'],
                                      description=vacancy['vacancyRichText']))
