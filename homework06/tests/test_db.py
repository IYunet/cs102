import pathlib
import sys
import typing as tp

import pytest
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

sys.path.append(str(pathlib.Path(__file__).parent.parent))
import db

test_news = [
    {
        "title": "TikTok overtakes Facebook as most downloaded app",
        "author": "em500",
        "url": "https://asia.nikkei.com/Business/Technology/TikTok-overtakes-Facebook-as-world-s-most-downloaded-app",
        "points": 558,
    },
    {
        "title": "New app",
        "author": "plefull",
        "url": "https://New.app.com",
        "points": 230,
    },
]

Base = declarative_base()


class News(Base):  # type: ignore
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    url = Column(String)
    points = Column(Integer)
    label = Column(String)


def db_set_up(engine):
    db.Base.metadata.create_all(bind=engine)


def db_tear_down(session):
    session.query(db.News).delete()
    session.commit()
    session.close()


def make_table_news(session: Session, news: tp.List[tp.Dict[str, tp.Union[int, str]]]) -> None:
    for i in range(len(news)):
        means = db.News(
            title=news[i]["title"],
            author=news[i]["author"],
            url=news[i]["url"],
            points=news[i]["points"],
        )
        session.add(means)
    session.commit()


@pytest.fixture
def engine():
    return create_engine("sqlite://")


@pytest.fixture
def session(engine):
    session = Session(engine)
    db_set_up(engine)
    yield session
    db_tear_down(session)


def test_news_can_be_saved(session):
    make_table_news(session=session, news=test_news)

    saved_item = session.query(db.News).get(1)
    assert saved_item.title == test_news[0]["title"]
    assert saved_item.author == test_news[0]["author"]

    saved_item = session.query(db.News).get(2)
    assert saved_item.title == test_news[1]["title"]
    assert saved_item.author == test_news[1]["author"]


def test_can_news_be_labeled(session):
    make_table_news(session=session, news=test_news)

    saved_item = session.query(db.News).get(1)
    assert saved_item.label is None

    label = "good"
    db.change_label(session=session, id=1, label=label)
    saved_item = session.query(db.News).get(1)
    assert saved_item.label == label
