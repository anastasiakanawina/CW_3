from abc import ABC, abstractmethod
import requests


class JobSiteAPI(ABC):

    @abstractmethod
    def get_vacancies(self, title):
        pass


class SuperJobAPI(JobSiteAPI):
    """ Получение вакансий из Superjob """
    def __init__(self):
        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        self.headers = {'X-Api-App-Id': 'v3.r.137788660.bcf4c0eedfe78070b7dfbac07a604d04144a2795.fd0f89da95e4c9625f8d2242faf0b5441201f763'}

    def get_vacancies(self, title=None):
        params = {'keywords': title}
        response = requests.get(self.url, headers=self.headers, params=params)
        data = response.json()

        return data['objects']


class HeadHunterAPI(JobSiteAPI):
    """ Получение вакансий из НН """
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies/'

    def get_vacancies(self, title):
        params = {'text': title}
        response = requests.get(self.url, params=params)
        data = response.json()

        return data['items']
