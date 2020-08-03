from brain_games.scripts import cli


description = 'What number is missing in the progression?'


def gen_progression(q=10):
    rand_pass = cli.gen_rand(1)
    rand_start = cli.gen_rand(nums_quantity=1, min_=1, max_=100)

    progress_list = list()
    progress_list.append(str(rand_start))

    while q:
        rand_start += rand_pass
        progress_list.append(str(rand_start))

        q -= 1

    return progress_list


def generate_question_answer_pair():
    progression = gen_progression()
    temp_progression = progression.copy()

    rand_index = cli.gen_rand(min_=0, max_=len(progression) - 1)
    temp_progression[rand_index] = '..'

    question = ' '.join(temp_progression)
    answer = str(progression[rand_index])

    return question, answer
