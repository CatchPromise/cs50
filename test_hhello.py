from hhello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("Promise") == "hello, Promise"