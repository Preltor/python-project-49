from random import randint, choice

QUESTION = 'What is the result of the expression?'


OPERATORS = ('+', '-', '*')


def make_calc(number_1, number_2, sign):
    if sign == '+':
        correct_answer = number_1 + number_2
    elif sign == '-':
        correct_answer = number_1 - number_2
    else:
        correct_answer = number_1 * number_2
    return correct_answer


def get_game():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    operator = choice(OPERATORS)
    correct_answer = make_calc(random_number1, random_number2, operator)
    question = f'Question: {random_number1} {operator} {random_number2}'
    return question, str(correct_answer)
