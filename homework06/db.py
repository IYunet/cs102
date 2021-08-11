import typing as tp

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from scraputils import get_news

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


def put_data_into_table(news_list: tp.List[tp.Dict[str, tp.Union[int, str]]]) -> None:
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


def change_label(session: Session, id: int, label: str) -> None:
    item = session.query(News).get(id)
    item.label = label
    session.commit()


if __name__ == "__main__":
    put_data_into_table(get_news("https://news.ycombinator.com/news", n_pages=2))
