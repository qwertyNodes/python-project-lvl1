import random


description = 'What number is missing in the progression?'


def gen_progression(quantity=10):
    rand_pass = random.randint(1, quantity)
    rand_start = random.randint(1, quantity * 10)

    progress_list = list()
    progress_list.append(str(rand_start))

    for _ in range(quantity):
        rand_start += rand_pass
        progress_list.append(str(rand_start))

    return progress_list


def generate_question_answer_pair():
    progression = gen_progression()
    temp_progression = progression.copy()

    rand_index = random.randint(0, len(progression) - 1)
    temp_progression[rand_index] = '..'

    question = ' '.join(temp_progression)
    answer = str(progression[rand_index])

    return question, answer
