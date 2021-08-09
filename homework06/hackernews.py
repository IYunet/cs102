import string

from bottle import redirect, request, route, run, template

from bayes import NaiveBayesClassifier
from db import News, change_label, put_data_into_table, session
from scraputils import get_news, get_news_more


@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template("news_template", rows=rows)


@route("/add_label/")
def add_label():
    s = session()
    id = request.query["id"]
    label = request.query["label"]
    change_label(s, id, label)
    redirect("/news")


counter_update_news = 3


@route("/update")
def update_news():
    global counter_update_news
    url = "https://news.ycombinator.com/news?p=" + str(counter_update_news)
    put_data_into_table(get_news_more(url))
    counter_update_news += 1
    redirect("/news")


colors = {"good": "#00d2fe", "never": "#180f3b", "maybe": "#969696"}


@route("/classify")
def classify_news():
    global colors
    s = session()
    model = NaiveBayesClassifier()
    train_set = s.query(News).filter(News.label != None).all()
    model.fit([clean(news.title).lower() for news in train_set], [news.label for news in train_set])
    test = s.query(News).filter(News.label == None).all()
    cell = list(map(lambda x: model.predict(x.title), test))
    return template(
        "color_template", rows=list(map(lambda x: (x[1], colors[cell[x[0]]]), enumerate(test)))
    )


def clean(s):
    translator = str.maketrans("", "", string.punctuation)
    return s.translate(translator)


if __name__ == "__main__":
    run(host="localhost", port=8080)
