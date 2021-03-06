def ask(message):
    return input(message + ' ')


def run(game):
    print('Welcome to the Brain Games!\n'
          '{}\n'.format(game.description))

    name = input('May i have your name: ')
    print('Hello, {}!\n'.format(name))
    error = False

    for _ in range(3):
        question, correct_answer = game.generate_question_answer_pair()
        user_answer = ask('Question: {}'.format(question))

        if user_answer != correct_answer:
            print('"{}" is wrong answer ;(. Correct answer was "{}".'
                  .format(user_answer, correct_answer))
            print('Let\'s try again, {}!'.format(name))
            error = True
            break

        print('Correct!')

    if not error:
        print('Congratulations, {}!'.format(name))
