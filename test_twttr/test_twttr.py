from twttr import shorten

def test_shorten():
    assert shorten("cat") == "ct"
    assert shorten("CAT") =="CT"
