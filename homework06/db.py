from sqlalchemy import Column, Integer, String, create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore

from scraputils import get_news  # type: ignore

Base = declarative_base()
engine = create_engine("sqlite:///news.db")
session = sessionmaker(bind=engine)


class News(Base):  # type: ignore
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    url = Column(String)
    points = Column(Integer)
    label = Column(String)


Base.metadata.create_all(bind=engine)


def put_data_into_table(news_list):
    s = session()
    for each_news in news_list:
        news = News(
            title=each_news["title"],
            author=each_news["author"],
            url=each_news["url"],
            points=each_news["points"],
        )
        s.add(news)
        s.commit()


def change_label(session, id, label):
    item = session.query(News).get(id)
    item.label = label
    session.commit()


if __name__ == "__main__":
    put_data_into_table(get_news("https://news.ycombinator.com/news", n_pages=2))
