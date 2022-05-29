import requests


def get_html(url: str):
    response = requests.get(url)
    content = response.text
    print(content)

