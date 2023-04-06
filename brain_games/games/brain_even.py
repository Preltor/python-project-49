from random import randint

QUESTION = ('Answer "yes" if the number is even, '
            'otherwise answer "no".')


def is_even(random_number):
    if random_number % 2 == 0:
        return True
    else:
        return False

def get_game():
    random_number = randint(0, 100)
    question = f'Question: {random_number}'
    if is_even(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
