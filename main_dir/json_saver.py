from abc import ABC, abstractmethod
import os
import json

path = os.path.join("database", "database.json")


class AbstractJobStorage(ABC):
    @abstractmethod
    def add_to_file(self, job):
        pass

    @abstractmethod
    def get_jobs(self, criteria):
        pass

    @abstractmethod
    def delete_job(self, job):
        pass


class JSONSaver(AbstractJobStorage):
    def add_to_file(self, data):
        if not os.path.isdir("database"):
            os.mkdir("database")

        # Чтение данных из файла (если файл существует)
        if os.path.isfile(path):
            with open(path, "r") as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        # Добавление новых данных
        existing_data.append(data)

        # Запись данных в файл
        with open(path, "w") as file:
            json.dump(existing_data, file, indent=2, ensure_ascii=False)

    def get_jobs(self, criteria):
        # Чтение данных из файла (если файл существует)
        if os.path.isfile(path):
            with open(path, "r") as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        filtered_jobs = []
        for job in existing_data:
            if all(job.get(key) == value for key, value in criteria.items()):
                filtered_jobs.append(job)
        return filtered_jobs

    def delete_job(self, vac_id):
        # Чтение данных из файла (если файл существует)
        if os.path.isfile(path):
            with open(path, "r") as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        # Удаление вакансии с указанным id
        updated_data = [job for job in existing_data if job.get("id") != vac_id]

        # Запись обновленных данных в файл
        with open(path, "w") as file:
            json.dump(updated_data, file, indent=2, ensure_ascii=False)
