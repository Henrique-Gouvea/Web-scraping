from tech_news.database import search_news
from datetime import datetime


def list_tuple(news_contain_title: list):
    return [(new["title"], new["url"]) for new in news_contain_title]


def search_insensitive(key: str, search: str) -> list:
    return search_news(
        {key: {"$regex": search, "$options": "i"}}
    )


def search_by_title(title: str) -> list:
    return list_tuple(search_insensitive('title', title))


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
    return list_tuple(search_insensitive('tags', tag))


def search_by_category(category):
    return list_tuple(search_insensitive('category', category))
