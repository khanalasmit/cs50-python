from twttr import shorten

def test_shorten():
    assert shorten("cat") == list("ct")
    assert shorten("hello") == list("hll")
    assert shorten("aeiou") == []
    assert shorten("AEIOU") == []
    assert shorten("Python") == list("Pythn")


