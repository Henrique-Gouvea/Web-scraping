import requests
import time
from parsel import Selector


def fetch(url: str) -> str:
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        time.sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


def scrape_novidades(html_content) -> list:
    selector = Selector(html_content)
    return selector.css("a.cs-overlay-link::attr(href)").getall()


def scrape_next_page_link(html_content) -> list:
    selector = Selector(html_content)
    return selector.css("a.next::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
