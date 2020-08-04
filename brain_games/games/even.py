import random


description = 'Answer "yes" if number even otherwise answer "no".'


def generate_question_answer_pair():
    rand_num = random.randint(1, 150)

    question = str(rand_num)
    correct_answer = 'yes' if rand_num % 2 == 0 else 'no'

    return question, correct_answer
