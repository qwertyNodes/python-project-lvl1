import random

import prompt


def meet_user(message):
    print('Welcome to the Brain Games!\n'
          '{}\n'.format(message))


def incorrect_answer_print(user_answer, correct_answer, name):
    print('"{}" is wrong answer ;(. Correct answer was "{}".'
          .format(user_answer, correct_answer))
    print('Let\'s try again, {}!'.format(name))


def get_name():
    name = prompt.string('May i have your name: ')
    print('Hello, {}!\n'.format(name))
    return name


def get_answer():
    return prompt.string('Your answer: ')


def congrat_message(name):
    print('Congratulations, {}!'.format(name))


def gen_rand(nums_quantity):
    rands = [random.randint(1, 10) for _ in range(nums_quantity)]
    return rands


def get_NOD(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1

    rest = None
    while rest != 0:
        rest = num1 % num2
        if rest == 0:
            return num2

        num1, num2 = num2, rest

    return None


def is_correct(ans1, ans2):
    return ans1 == ans2