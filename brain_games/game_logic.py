import prompt


def game(start_game):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')
    print(start_game.QUESTION)
    won_games = 0
    while won_games < 3:
        question, correct_answer = start_game.get_game()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(correct_answer):
            print('Correct')
            won_games += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct "
                  f"answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
        print(f'Congratulations, {name}!')
