import typing as tp

import requests  # type: ignore
from bs4 import BeautifulSoup


def extract_news(parser: BeautifulSoup) -> tp.List[tp.Dict[str, tp.Union[int, str]]]:
    """Extract news from a given web page"""
    url = "https://news.ycombinator.com/"

    news_list = []
    title_list = []
    links_list = []
    author_list = []
    points_list = []

    title = parser.select(".storylink")
    points = parser.select(".score")
    subtext = parser.select(".subtext")

    for i in title:
        title_list.append(i.text)
        link = i.get("href", None)
        if link.startswith("item"):
            links_list.append(url + link)
        else:
            links_list.append(link)

    for i in range(len(subtext)):
        author = subtext[i].select(".hnuser")
        if author == []:
            author = "Anonymous"
        else:
            author = author[0].text
        author_list.append(author)

        points = subtext[i].select(".score")
        if points == []:
            points = 0
        else:
            points = int(points[0].text.split()[0])
        points_list.append(points)

    for i in range(len(title)):
        news_list.append(
            {
                "title": title_list[i],
                "url": links_list[i],
                "author": author_list[i],
                "points": points_list[i],
            }
        )
    return news_list


def extract_next_page(n_pages):
    """Extract next page URL"""
    return "news?p={}".format(n_pages)


def get_news(url, n_pages=1):
    """Collect news from a given web page"""
    news = []
    n_pages_requer = 2
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(n_pages_requer)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
        n_pages_requer += 1
    return news


def get_news_more(url):

    news = []
    print("Collecting data from page: {}".format(url))
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    news_list = extract_news(soup)
    news.extend(news_list)
    return news
