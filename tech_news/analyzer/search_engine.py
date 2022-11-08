from tech_news.database import search_news
from datetime import datetime


def list_tuple(news_contain_title: list):
    return [(new["title"], new["url"]) for new in news_contain_title]


def search_by_title(title: str) -> list:
    news_contain_title: list = search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    return list_tuple(news_contain_title)


def search_by_date(date: str) -> list:
    try:
        date_formated = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        news_contain_date: list = search_news(
            {"timestamp": {"$eq": date_formated}}
        )
        return list_tuple(news_contain_date)
    except ValueError:
        raise ValueError("Data inválida")


def search_by_tag(tag: str) -> list:
    news_contain_tag: list = search_news(
        {"tags": {'$regex': tag, '$options': 'i'}}
    )
    return list_tuple(news_contain_tag)


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
