import random

import prompt


def meet_user(message):
    print('Welcome to the Brain Games!\n'
          '{}\n'.format(message))


def is_simple(num):
    count = 2

    for i in range(2, num):
        res = num % i
        if res == 0:
            return False
    return True


def ask_something(message):
    return prompt.string(message)


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


def gen_rand(nums_quantity, min_=1, max_=10):
    rands = [random.randint(min_, max_) for _ in range(nums_quantity)] \
            if nums_quantity > 1 else random.randint(min_, max_)
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


def gen_progression(q=10):
    rand_pass = gen_rand(1)
    rand_start = gen_rand(nums_quantity=1, min_=1, max_=100)

    progress_list = list()
    progress_list.append(rand_start)

    while q:
        rand_start += rand_pass
        progress_list.append(rand_start)

        q -= 1

    return progress_list
