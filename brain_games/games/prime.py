import random


description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_simple(num):
    for i in range(2, num):
        res = num % i
        if res == 0:
            return False
    return True


def generate_question_answer_pair():
    num = random.randint(3, 100)

    question = str(num)
    answer = 'yes' if is_simple(num) else 'no'

    return question, answer
