from app.handler import fizzbuzz


def test_fizzbuzz_fizz():
    assert fizzbuzz(3) == 'Fizz'


def test_fizzbuzz_buzz():
    assert fizzbuzz(5) == 'Buzz'


def test_fizzbuzz_fizzbuzz():
    assert fizzbuzz(15) == 'FizzBuzz'


def test_fizzbuzz_num():
    assert fizzbuzz(1) == '1'
