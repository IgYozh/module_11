# requests, matplotlib, numpy
import requests
import matplotlib
from matplotlib.figure import Figure
import numpy

# REQUESTS: Использование класса requests.Session

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()  # Инициализируем сессию

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url)
        response.raise_for_status()  # Поднимаем исключение, если код ответа не 200
        return response.json()

    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()

# Пример использования:
client = ApiClient("https://jsonplaceholder.typicode.com")
print(client.get("posts/1"))  # Получаем данные для поста с id=1
print(client.post("posts", {"title": "foo", "body": "bar", "userId": 1}))  # Создаём новый пост

# REQUESTS: Использование метода requests.get

def fetch_user_data(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)  # Используем метод GET для запроса
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch data. Status code: {response.status_code}"}

# Пример использования:
print(fetch_user_data(1))  # Загружаем данные пользователя с ID 1

# REQUESTS: Использование функции requests.request

def send_custom_request(method, url, **kwargs):
    response = requests.request(method, url, **kwargs)  # Используем функцию request
    if response.status_code == 200:
        return response.text  # Возвращаем текст ответа
    else:
        return f"Error: {response.status_code}"

# Пример использования:
url = "https://jsonplaceholder.typicode.com/posts/1"
print(send_custom_request("GET", url))  # Отправляем GET-запрос
print(send_custom_request("DELETE", url))  # Отправляем DELETE-запрос




# Использование класса matplotlib.figure.Figure


