from brain_games.scripts import cli
from brain_games.games import progression as prog
from brain_games.games import calc
from brain_games.games import even
from brain_games.games import gcd
from brain_games.games import prime


def start_progression():
    run(prog)


def start_calc():
    run(calc)


def start_even():
    run(even)


def start_gcd():
    run(gcd)


def start_prime():
    run(prime)


def run(game):
    cli.meet_user(game.description)
    name = cli.get_name()
    count = 0
    while count < 3:
        question, correct_answer = game.generate_question_answer_pair()
        user_answer = cli.ask_question('Question: {}'.format(question))

        if user_answer != correct_answer:
            cli.incorrect_answer_print(correct_answer, user_answer, name)
            break

        print('Correct!')
        count += 1

    if count == 3:
        print('Congratulations, {}!'.format(name))
