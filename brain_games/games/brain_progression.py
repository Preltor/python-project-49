from random import randint

QUESTION = 'What number is missing in the progression?'


def gen_progression(number):
    first_num = randint(1, 77)
    step = randint(3, 11)
    ls = []
    total = number
    while total:
        ls.append(first_num)
        first_num += step
        total -= 1
    return ls


def get_game():
    length = randint(8, 11)
    ls = gen_progression(length)
    random_index = randint(0, length - 1)
    correct_answer: str = ls[random_index]
    ls[random_index] = '..'
    str_progression = " ".join(map(str, ls))
    question = f'Question: {str_progression}'
    return question, correct_answer
