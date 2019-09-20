from app.handler import lambda_handler


def test_handler_fizzbuzz():
    event = {"num": 15}
    assert lambda_handler(event, "") == 'FizzBuzz'


def test_handler_num():
    event = {"num": 2}
    assert lambda_handler(event, "") == '2'
