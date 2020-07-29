import prompt


def meet_user(message):
    print('Welcome to the Brain Games!\n'
          '{}\n'.format(message))


def print_incorrect_answer(user_answer, correct_answer, name):
    print('"{}" is wrong answer ;(. Correct answer was "{}".'
          .format(user_answer, correct_answer))
    print('Let\'s try again, {}!'.format(name))


def ask_name():
    name = prompt.string('May i have your name: ')
    print('Hello, {}!\n'.format(name))
    return name


def get_answer():
    return prompt.string('Your answer: ')


def congrat_message(name):
    print('Congratulations, {}!'.format(name))
