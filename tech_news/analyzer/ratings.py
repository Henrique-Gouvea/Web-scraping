from tech_news.database import find_news
from tech_news.analyzer.search_engine import list_tuple
from collections import Counter


def top_5_news() -> list:
    news: list = find_news()
    news.sort(
        key=lambda row: (row["comments_count"], row["title"]), reverse=True
    )
    return list_tuple(news[:5])


# Requisito 11
def top_5_categories() -> list:
    news: list = find_news()
    category_counter: list = Counter([new["category"] for new in news])
    order_categories: list = sorted(
        category_counter.items(), key=lambda row: (-row[1], row[0])
    )
    categories_list: list = list(category[0] for category in order_categories)

    return categories_list[:5]
