from random import randint

QUESTION = 'Find the greatest common divisor of given numbers.'


def make_gcd(number_1, number_2):
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 = number_1 % number_2
        else:
            number_2 = number_2 % number_1
    correct_answer = number_1 + number_2
    return correct_answer


def get_game():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    correct_answer = make_gcd(random_number1, random_number2)
    question = f'Question: {random_number1} {random_number2}'
    return question, str(correct_answer)
