from twttr import shorten

def test_shorten():
    assert shorten("cat") == "ct"
    assert shorten("CAT") =="CT"
    assert shorten("CAT1")=="CT1"
    assert shorten("CA!1")=="C!1"
