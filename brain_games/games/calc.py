import random

from brain_games.scripts import cli


description = 'What is the result of the expression?'


def add(num1, num2):
    return num1 + num2


def dev(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def calc_answ(num1, num2, operation):
    return operation(num1, num2)


def generate_question_answer_pair():
    operations = [('+', add), ('-', dev), ('*', mult)]

    operation = random.choice(operations)
    num1, num2 = cli.gen_rand(2)

    if operation[0] == '-' and num1 < num2:
        num1, num2 = num2, num1

    question = str(num1) + ' ' + operation[0] + ' ' + str(num2)
    correct_answer = calc_answ(num1, num2, operation[1])

    return question, str(correct_answer)
