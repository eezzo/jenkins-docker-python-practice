import requests


def get_web_page(url):
    r = requests.get(url)
    return r

