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


def scrape_noticia(html_content):
    selector = Selector(html_content)
    comment = selector.css("h5.title-block::text").get()
    quantity_comments = (
        comment.split()[0] if (comment.split()[0] != "Arquivos") else 0
    )

    return {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        # rstrip cópia da string com os caracteres finais removidos.
        "title": selector.css("h1.entry-title::text").get().rstrip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("a.url::text").get(),
        "comments_count": quantity_comments,
        "summary": selector.xpath("string(//p)").get().rstrip(),
        "tags": selector.css(".post-tags a::text").getall(),
        "category": selector.css("span.label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
