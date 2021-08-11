import pathlib
import sys

import requests
from bs4 import BeautifulSoup

sys.path.append(str(pathlib.Path(__file__).parent.parent))

import scraputils


def test_extrat_news() -> None:
    expample = """</tr></table></td></tr>
    <tr id="pagespace" style="height:10px" title=""></tr><tr><td><table border="0" cellpadding="0" cellspacing="0" class="itemlist">    
    <tr class="athing" id="28133017">
    <td align="right" class="title" valign="top"><span class="rank">1.</span></td> <td class="votelinks" valign="top"><center><a href="vote?id=28133017&amp;how=up&amp;goto=news" id="up_28133017"><div class="votearrow" title="upvote"></div></a></center></td><td class="title"><a class="storylink" href="https://asia.nikkei.com/Business/Technology/TikTok-overtakes-Facebook-as-world-s-most-downloaded-app">TikTok overtakes Facebook as most downloaded app</a><span class="sitebit comhead"> (<a href="from?site=nikkei.com"><span class="sitestr">nikkei.com</span></a>)</span></td></tr><tr><td colspan="2"></td><td class="subtext">
    <span class="score" id="score_28133017">558 points</span> by <a class="hnuser" href="user?id=em500">em500</a> <span class="age" title="2021-08-10T19:21:14"><a href="item?id=28133017">5 hours ago</a></span> <span id="unv_28133017"></span> | <a href="hide?id=28133017&amp;goto=news">hide</a> | <a href="item?id=28133017">354 comments</a> </td></tr>
    <tr class="spacer" style="height:5px"></tr>"""
    soup = BeautifulSoup(expample, "html.parser")
    expexted_news = [
        {
            "author": "em500",
            "points": 558,
            "title": "TikTok overtakes Facebook as most downloaded app",
            "url": "https://asia.nikkei.com/Business/Technology/TikTok-overtakes-Facebook-as-world-s-most-downloaded-app",
        }
    ]
    getted_news = scraputils.extract_news(soup)

    assert expexted_news == getted_news


def test_get_news() -> None:
    news = []
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    current_news = scraputils.extract_news(soup)
    next_url = scraputils.extract_next_page(soup)
    url = "https://news.ycombinator.com/" + next_url
    news.extend(current_news)

    assert scraputils.get_news("https://news.ycombinator.com/") == news


def test_extract_next_page() -> None:
    number = 5
    excepcted = "news?p={}".format(number)
    current_value = scraputils.extract_next_page(number)

    assert excepcted == current_value


def test_get_news_more() -> None:
    news = []
    url = "https://news.ycombinator.com/news?p=3"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    current_news = scraputils.extract_news(soup)
    news.extend(current_news)

    assert scraputils.get_news_more("https://news.ycombinator.com/news?p=3") == news
