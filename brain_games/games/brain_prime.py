from random import randint

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


def get_game():
    random_number = randint(1, 100)
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = f'Question: {random_number}'
    return question, correct_answer
