from tech_news.database import find_news
from tech_news.analyzer.search_engine import list_tuple


def top_5_news() -> list:
    news: list = find_news()
    news.sort(
        key=lambda row: (row["comments_count"], row["title"]), reverse=True
    )
    return list_tuple(news[:5])


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
