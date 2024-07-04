from demo import shorten

def test_shorten():
    assert shorten("cat") == list("ct")
    assert shorten("hello") == list("hll")
    assert shorten("aeiou") == []
    assert shorten("AEIOU") == []
    assert shorten("Python") == list("Pythn")

if __name__ == "__main__":
    test_shorten()
    print("All tests passed!")

