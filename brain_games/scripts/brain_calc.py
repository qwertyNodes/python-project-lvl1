import random

from brain_games import cli


def add(num1, num2):
    return num1 + num2


def dev(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def calc_answ(num1, num2, operation):
    return operation(num1, num2)


def ask_question(name):
    operations = [('+', add), ('-', dev), ('*', mult)]

    num1, num2, operation = random.randint(1, 10), random.randint(1, 10), random.choice(operations)

    if operation[0] == '-' and num1 < num2:
        num1, num2 = num2, num1

    calc_answer = calc_answ(num1, num2, operation[1])

    print('Question: {} {} {}'.format(num1, operation[0], num2))
    user_answer = int(cli.get_answer())

    if calc_answer == user_answer:
        print('Correct!')
        return True

    cli.print_incorrect_answer(user_answer, calc_answer, name)
    return False


def main():
    cli.meet_user('What is the result of the expression?')
    name = cli.ask_name()
    count = 1

    while ask_question(name) and count < 3:
        count += 1

    if count == 3:
        cli.congrat_message(name)


if __name__ == '__main__':
    main()
