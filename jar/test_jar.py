import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(20)
    assert jar.capacity == 20

    with pytest.raises(ValueError):
        Jar(-5)

    with pytest.raises(ValueError):
        Jar("not an integer")

def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    jar.deposit(3)
    assert jar.size == 8

    with pytest.raises(ValueError):
        jar.deposit(5)  # Exceeds capacity of 12

def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(3)
    assert jar.size == 5

    jar.withdraw(5)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(1)  # Not enough cookies
