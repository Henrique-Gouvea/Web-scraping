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
def top_5_categories():
    news: list = find_news()
    teste = []
    for new in news:
        print(new["tags"])
        teste.extend(new["tags"])
    henrique = Counter(teste)
    teste2 = []
    for i in sorted(henrique, key=henrique.get, reverse=True):
        teste2.append(i)
    print(henrique)
    print(teste2)
    return teste2[:5]
