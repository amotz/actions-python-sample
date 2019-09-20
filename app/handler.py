def lambda_handler(event, context):
    num = event['num']

    return fizzbuzz(num)


def fizzbuzz(num):
    if num % 15 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'

    return str(num)
