import requests


def fetch(url: str):
    try:
        response = requests.get(url, timeout=1)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return ''
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
