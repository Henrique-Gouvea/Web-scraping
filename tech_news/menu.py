from tech_news.analyzer.ratings import top_5_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import search_by_title
from tech_news.analyzer.search_engine import search_by_date
from tech_news.analyzer.search_engine import search_by_tag
from tech_news.analyzer.search_engine import search_by_category
import sys


def get_menu():
    escolha: int = input(
        """
        Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.
 """
    )
    return int(escolha) if escolha != '' else 999


def analyzer_menu():
    escolha = get_menu()
    if escolha == 0:
        quantity_news: str = input("Digite quantas notícias serão buscadas:")
        print(get_tech_news(quantity_news))
        pass
    if escolha == 1:
        title: str = input("Digite o título:")
        print(search_by_title(title))
        pass
    elif escolha == 2:
        date: str = input("Digite a data no formato aaaa-mm-dd:")
        print(search_by_date(date))
        pass
    elif escolha == 3:
        tag: str = input("Digite a tag:")
        print(search_by_tag(tag))
        pass
    elif escolha == 4:
        category: str = input("Digite a categoria:")
        print(search_by_category(category))
        pass
    elif escolha == 5:
        print(top_5_news())
        pass
    elif escolha == 6:
        print(top_5_categories())
        pass
    elif escolha == 7:
        print("Encerrando script\n")
        # sys.exit("Encerrando script\n")
        exit()
    else:
        sys.stderr.write("Opção inválida")
