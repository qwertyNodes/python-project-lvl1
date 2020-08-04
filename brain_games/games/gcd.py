import random


description = 'Find the greatest common divisor of given numbers.'


def get_gcd(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1

    rest = None
    while rest != 0:
        rest = num1 % num2
        if rest == 0:
            return num2

        num1, num2 = num2, rest

    return None


def generate_question_answer_pair():
    num1, num2 = random.randint(0, 10), random.randint(0, 10)

    question = '{} {}'.format(num1, num2)
    answer = str(get_gcd(num1, num2))

    return question, answer
