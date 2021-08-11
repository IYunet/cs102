import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent.parent))
import hackernews


def test_clear() -> None:
    assert hackernews.clean("CAT") == "CAT"
    assert hackernews.clean("C, A, T") == "C A T"
    assert hackernews.clean("CAT(and)DOG") == "CATandDOG"
